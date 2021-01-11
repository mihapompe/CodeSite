import bottle
from  model import *
import datetime
import os


@bottle.get("/")
def index():
    return bottle.redirect("/login")

@bottle.get("/modules")
def main_page(username = ""):
    user = get_user_from_cookie(username = username)
    user.automatic_module_updates()
    save_user(user)
    modules_list = read_modules()
    return bottle.template("views/modules.tpl", modules_list = modules_list, user = user)

@bottle.get('/login')
def login():
    if bottle.request.get_cookie("user_cookie") and bottle.request.get_cookie("remember_me") == "True":
        print("You already have a cookie.")
        print(bottle.request.get_cookie("user_cookie"))
        bottle.redirect("/modules")
    return bottle.template("views/login.tpl")

@bottle.post('/login')
def do_login():
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    remember_me = bool(bottle.request.forms.get('remember_me'))
    if check_login(username, password):
        today = datetime.date.today()
        bottle.response.set_cookie("user_cookie", username, expires=datetime.date(today.year+1, today.month, today.day))
        bottle.response.set_cookie("remember_me", str(remember_me), expires=datetime.date(today.year+1, today.month, today.day))
        bottle.redirect("/modules")
    else:
        return "<p>Login failed. You entered a wrong username or password.</p>"

@bottle.get("/modules/module<module_number:int>")
def module_page(module_number):
    modules_list = read_modules()
    module = modules_list[int(module_number)-1]
    user = get_user_from_cookie()
    file_path = "download/"
    for exercise in module.exercises:
        for file_name in exercise.download_files:
            if os.path.exists(file_path+user.username+file_name) and user.username != "":
                os.remove(file_path+user.username+file_name)
    return bottle.template("views/module.tpl", module = module, user = user)

@bottle.get("/static/<file_name:path>")
def serve_static(file_name):
    return bottle.static_file(file_name, root="static/")

@bottle.get("/instructions")
def instructions_page():
    return bottle.template("views/instructions.tpl", user = get_user_from_cookie())

@bottle.get("/about")
def instructions_page():
    return bottle.template("views/about.tpl", user = get_user_from_cookie())

@bottle.get("/license")
def instructions_page():
    return bottle.template("views/license.tpl", user = get_user_from_cookie())

@bottle.get("/debugging")
def instructions_page():
    return bottle.template("views/debugging.tpl", user = get_user_from_cookie())

@bottle.get("/download_exercises/<module_number:int>/<exercise_number:int>")
def download(module_number, exercise_number):
    modules_list = read_modules()
    exercise = modules_list[int(module_number)-1].exercises[int(exercise_number)-1]
    file_name = exercise.download_files[0]
    return bottle.static_file(file_name, root="download/", download=file_name)

@bottle.get("/download_tester/<module_number:int>/<exercise_number:int>")
def download(module_number, exercise_number):
    modules_list = read_modules()
    exercise = modules_list[int(module_number)-1].exercises[int(exercise_number)-1]
    file_name = exercise.download_files[1]
    username = get_user_from_cookie().username
    personalize_file(file_name, module_number, exercise_number, username)
    return bottle.static_file(username+file_name, root="download/", download=username+file_name)

@bottle.get("/download/<filename>")
def download(filename):
    return bottle.static_file(filename, root="download/", download=filename)

@bottle.get("/mark_as_completed/<module_number:int>/<exercise_number:int>")
def mark_as_completed(module_number, exercise_number):
    results = {
        "module_number": int(module_number),
        "exercise_number": int(exercise_number),
        "score": 100
    }
    user = get_user_from_cookie()
    append_results(user.username, results)
    return bottle.redirect("/modules/module{}".format(module_number))

@bottle.get("/templates")
def instructions_page():
    return bottle.template("views/templates.tpl", user = get_user_from_cookie())

@bottle.get("/logout")
def logout():
    delete_cookie()
    return bottle.template("views/login.tpl")

@bottle.get("/stats")
def stats_page():
    return bottle.template("views/stats.tpl", user = get_user_from_cookie())

@bottle.get("/stats/<username>")
def admin_stats_page(username):
    return bottle.template("views/admin_stats.tpl", user = get_user_from_cookie(), user_ = get_user_from_username(username))

@bottle.post("/exercise_results/<username>")
def gather_results(username):
    for i in bottle.request.body:
        t = str(i).split("'")
    t.pop(0)
    t.pop(-1)
    t = t[0].split("&")
    results = {}
    for i in t:
        a = i.split("=")
        results[a[0]] = int(a[1])
    append_results(username, results)
    return

@bottle.get("/profile")
def profile():
    user = get_user_from_cookie()
    return bottle.template("views/profile.tpl", user = user)

@bottle.get("/dashboard")
def profile():
    user = get_user_from_cookie()
    users = load_users()
    if user.admin == True:
        return bottle.template("views/dashboard.tpl", user = user, users = users)
    return bottle.redirect("/modules")

@bottle.get("/add_user")
def add_user():
    user = get_user_from_cookie()
    if user.admin == True:
        return bottle.template("views/add_user.tpl", user = user)
    return bottle.redirect("/modules")

@bottle.post("/add_user")
def post_user():
    name = bottle.request.forms.get('name')
    surname = bottle.request.forms.get('surname')
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    mail = bottle.request.forms.get('mail')
    year = bottle.request.forms.get('starting_date_year')
    month = bottle.request.forms.get('starting_date_month')
    day = bottle.request.forms.get('starting_date_day')
    admin = bottle.request.forms.get('admin')
    add_new_user(User(
        name = name,
        surname = surname,
        username = username,
        password = password,#encrypt_password(password),
        mail = mail,
        starting_date = [int(year), int(month), int(day)],
        admin = bool(admin)
    ))
    bottle.redirect("/dashboard")
    return

@bottle.get("/add_exercise/<module_number:int>")
def add_exercise_page(module_number):
    user = get_user_from_cookie()
    modules = read_modules()
    next_exercise_number = modules[int(module_number)-1].exercises[-1].exercise_number+1
    if user.admin == True:
        return bottle.template("views/add_exercise.tpl", user = user, module_number = module_number, exercise_number = next_exercise_number)
    return bottle.redirect("/modules")

@bottle.post("/add_exercise/<module_num:int>")
def post_exercise(module_num):
    module_number = bottle.request.forms.get('module_number')
    exercise_number = bottle.request.forms.get('exercise_number')
    title = bottle.request.forms.get('title')
    description = bottle.request.forms.get('description')
    exercise_type = bottle.request.forms.get('type')
    uploads = bottle.request.files.getall('test_files')
    test_files = []
    for upload in uploads:
        name, ext = os.path.splitext(upload.filename)
        test_files.append(upload.filename)
        if ext not in ('.py', '.jpg', '.jpeg', '.zip'):
            return "File extension not allowed."
        save_path = "download"
        file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
        upload.save(file_path)
    add_exercise(module_number, Exercise(
        title = title,
        description = description,
        exercise_number = exercise_number,
        subexercises = [],
        download_files = test_files,
        exercise_type = exercise_type
    ))
    bottle.redirect("/modules/module{}".format(module_num))
    return

@bottle.get("/<module_number:int>/<exercise_number:int>")
def add_subexercise(module_number, exercise_number):
    user = get_user_from_cookie()
    if user.admin == True:
        return bottle.template("views/add_subexercise.tpl", user = user, module_number = module_number, exercise_number = exercise_number)
    return main_page()

@bottle.post("/add_subexercise")
def post_subexercise():
    module_number = int(bottle.request.forms.get('module_number'))
    exercise_number = int(bottle.request.forms.get('exercise_number'))
    description = bottle.request.forms.get('description')
    modules = read_modules()
    for module in modules:
        if module.module_number == module_number:
            for exercise in module.exercises:
                if exercise.exercise_number == exercise_number:
                    exercise.subexercises.append(description)
                    update_exercise(module_number, exercise)
                    return bottle.redirect("/modules/module{}".format(module_number))
    print("Subexercise not created, check module and exercise numbers.")
    return bottle.redirect("/{}/{}".format(module_number, exercise_number))




bottle.run(debug = True, reloader= True)
