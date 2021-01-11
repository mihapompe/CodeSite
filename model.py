import json
import time
import bottle
import datetime
from passlib.hash import pbkdf2_sha256

# These constants should be adjusted when adding a new module or exercise.
NUMBER_OF_MODULES = 3
NUMBER_OF_EXERCISES = [4,1,1]

# =============================================================================
# User
# This object contains all the user information and methods for it's operation.
# Following the object decleration are some functions used on a set of users.
# =============================================================================

class User():
    def __init__(self, name, surname, username, password, mail, starting_date, enabled_modules = [1], admin = False, progress = [[0 for j in range(i)] for i in NUMBER_OF_EXERCISES]):
        self.name = name                        # first name
        self.surname = surname                  # surname
        self.username = username                # username
        self.password = password                # password, encrypted SHA256
        self.mail = mail                        # str, mail
        self.enabled_modules = enabled_modules  # list of enabled modules.
        self.progress = progress                # 2D list, gives you the progress for a given exercise in %.
        self.admin = admin                      # True if the user is admin
        self.starting_date = datetime.date(year = starting_date[0], month = starting_date[1], day = starting_date[2])  #[year, month, day]

    def __repr__(self):
        return "{} {} {} {}".format(self.name, self.surname, self.username, self.mail)

    def days_since_start(self):
        delta = datetime.date.today() - self.starting_date
        return delta.days

    def automatic_module_updates(self):
        if self.days_since_start()//7 == len(self.enabled_modules):
            self.unlock_next_module()
        return

    def unlock_next_module(self):
        if self.enabled_modules[-1] != NUMBER_OF_MODULES:
            self.enabled_modules.append(self.enabled_modules[-1]+1)
            self.progress.append([0 for i in range(NUMBER_OF_EXERCISES[self.enabled_modules[-1]-1])])
            return

    @staticmethod
    def user_from_dict(dictionary):
        return User(
            name = dictionary["name"],
            surname = dictionary["surname"],
            username = dictionary["username"],
            password = dictionary["password"],
            mail = dictionary["mail"],
            enabled_modules = dictionary["enabled_modules"],
            admin = dictionary["admin"],
            progress = dictionary["progress"],
            starting_date = dictionary["starting_date"]
        )

    def user_to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password,
            "mail": self.mail,
            "enabled_modules": self.enabled_modules,
            "progress": self.progress,
            "admin": self.admin,
            "starting_date": [self.starting_date.year, self.starting_date.month, self.starting_date.day]
        }

    def global_progress(self):
        result = 0
        for exercise_result in self.progress:
            result += sum(exercise_result)/len(exercise_result)
        return round(result/NUMBER_OF_MODULES,1)

def add_new_user(user):
    users = load_users()
    users.append(user)
    save_users(users)
    return

def load_users():
    file_name = "data/users.json"
    users_list = []
    with open(file_name, "r") as users_file:
        users_dict = json.load(users_file)
    for user in users_dict["users"]:
        users_list.append(User.user_from_dict(user))
    return users_list

def save_users(users_list):
    file_name = "data/users.json"
    dict_out = {}
    users_dict_list = []
    for user in users_list:
        users_dict_list.append(user.user_to_dict())
    dict_out["users"] = users_dict_list
    with open(file_name, "w") as users_file:
        return users_file.write(json.dumps(dict_out, ensure_ascii=False, indent=4))

def save_user(user):
    users = load_users()
    for i, old_user in enumerate(users):
        if old_user.username == user.username:
            users[i] = user
    save_users(users)
    return

def encrypt_password(password):
    return pbkdf2_sha256.hash(password)

def check_login(username, password):
    users = load_users()
    correct = False
    for user in users:
        if user.username == username and pbkdf2_sha256.verify(password, user.password):
            return True
    return False

def get_user_from_username(username):
    users = load_users()
    for user in users:
        if user.username == username:
            return user
    return None

def get_user_from_cookie(username = ""):
    if username == "":
        username = bottle.request.get_cookie("user_cookie")
    return get_user_from_username(username)

def delete_cookie():
    bottle.response.delete_cookie("user_cookie")

def append_results(username, results):
    users = load_users()
    index = 0
    for i in range(len(users)):
        if users[i].username == username:
            index = i
    users[index].progress[results["module_number"]-1][results["exercise_number"]-1] = results["score"]
    save_users(users)
    return

def personalize_file(file_name, module_number, exercise_number, username):
    file_path = "download/"
    tester_code = "import requests \nr = requests.post('http://127.0.0.1:8080/exercise_results/" + username + "', data={\'module_number\': "+str(module_number)+", \'exercise_number\': " + str(exercise_number) + ", \'score\': score})"
    with open(file_path+file_name, "r") as file:
        content = file.read()
    with open(file_path+username+file_name, "w") as file:
        file.write(content + "\n" + tester_code)
    return

# =============================================================================
# Exercise
# This object contains all information about a certain exercise.
# =============================================================================

class Exercise():
    def __init__(self, title, description, exercise_number, subexercises, download_files, exercise_type = "exercise", video_file=""):
        self.title = title                      # title of the exercise, e.g. "Loops"
        self.description = description          # description
        self.exercise_number = exercise_number  # starting with 1
        self.subexercises = subexercises        # list of subexercises, string
        self.download_files = download_files    # list of file names, e.g. loops_tester.py
        self.type = exercise_type               # ["exercise", "text", "video"]
        self.video_file = video_file

    def __repr__(self):
        return self.title

    def exercise_to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "exercise_number": int(self.exercise_number),
            "subexercises": self.subexercises,
            "download_files": self.download_files,
            "exercise_type": self.type,
            "video_file": self.video_file
        }

    @staticmethod
    def exercise_from_dict(dictionary):
        return Exercise(
            title = dictionary["title"],
            description = dictionary["description"],
            exercise_number = int(dictionary["exercise_number"]),
            subexercises = dictionary["subexercises"],
            download_files = dictionary["download_files"],
            exercise_type = dictionary["exercise_type"],
            video_file = dictionary["video_file"]
        )

def add_exercise(module_number, exercise):
    modules = read_modules()
    modules[int(module_number)-1].exercises.append(exercise)
    modules[int(module_number)-1].save_module()
    return

def update_exercise(module_number, exercise):
    modules = read_modules()
    modules[int(module_number)-1].exercises[exercise.exercise_number-1] = exercise
    modules[int(module_number)-1].save_module()
    return

# =============================================================================
# Module
# This object contains a set of exercises with some additional metadata.
# =============================================================================

class Module():
    def __init__(self, title, module_number, exercises, description = ""):
        self.title = title                      # module title
        self.module_number = module_number      # module number starting with 1, ...
        self.description = description          # module description
        self.exercises = exercises              # list of exercises

    def __repr__(self):
        return self.title

    def module_to_dict(self):
        return {
            "title": self.title,
            "module_number": self.module_number,
            "description": self.description,
            "exercises": [exercise.exercise_to_dict() for exercise in self.exercises]
        }

    def save_module(self):
        file_name = "data/module{}.json".format(self.module_number)
        with open(file_name, "w") as module_file:
            return module_file.write(json.dumps(self.module_to_dict(), ensure_ascii=False, indent=4))

    @staticmethod
    def dict_to_module(dictionary):
        return Module(
            title = dictionary["title"],
            module_number = int(dictionary["module_number"]),
            description = dictionary["description"],
            exercises = [Exercise.exercise_from_dict(exercise) for exercise in dictionary["exercises"]]
        )

    @staticmethod
    def upload_module(module_number):
        file_name = "data/module{}.json".format(module_number)
        with open(file_name, "r") as module_file:
            return Module.dict_to_module(json.loads(module_file.read()))

def read_modules():
    modules_list = []
    for i in range(1, NUMBER_OF_MODULES+1):
        modules_list.append(Module.upload_module(i))
    return modules_list









































# Unused functions

# def upload_exercises():
#     file_name = "data/exercises.json"
#     exercises_out = []
#     with open(file_name, "r") as exercises_file:
#         exercises_dict = json.load(exercises_file)
#     for exercise in exercises_dict:
#         exercises_out.append(Exercise.exercise_from_dict(exercise))
#     return exercises_out

# def save_exercises(exercises_list):
#     file_name = "data/exercises.json"
#     dict_out = {}
#     exercises_dict_list = []
#     for exercise in exercises_list:
#         exercises_dict_list.append(exercise.exercise_to_dict())
#     dict_out["exercises"] = exercises_dict_list
#     with open(file_name, "w") as exercises_file:
#             return exercises_file.write(json.dumps(dict_out, exercises_file, ensure_ascii=False, indent=4))