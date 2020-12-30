import json


NUMBER_OF_MODULES = 1



class User():
    def __init__(self, name, surname, username, password, mail, enabled_modules = [1], admin = False):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.mail = mail
        self.enabled_modules = enabled_modules
        #self.progress = 
        self.admin = admin

    def __repr__(self):
        return "{} {}".format(self.name, self.surname)

    def unlock_next_module(self):
        if self.enabled_modules[-1] != NUMBER_OF_MODULES:
            self.enabled_modules.append(self.enabled_modules[-1]+1)
            return True
        else:
            return False

    @staticmethod
    def user_from_dict(dictionary):
        return

    def user_to_dict(self):
        return


def load_users():
    return

def check_login(username, password):
    return True


class Exercise():
    def __init__(self, title, exercise_number, subexercises, download_files, exercise_type = "exercise"):
        self.title = title                      # title of the exercise, e.g. "Loops"
        self.exercise_number = exercise_number  # starting with 1
        self.subexercises = subexercises        # list of subexercises, string
        self.download_files = download_files    # list of file names, e.g. loops_tester.py
        self.type = exercise_type               # ["exercise", "text", "video"]

    def __repr__(self):
        return self.title

    def exercise_to_dict(self):
        return {
            "title": self.title,
            "exercise_number": self.exercise_number,
            "subexercises": self.subexercises,
            "download_files": self.download_files,
            "exercise_type": self.type
        }

    @staticmethod
    def exercise_from_dict(dictionary):
        return Exercise(
            title = dictionary["title"],
            exercise_number = dictionary["exercise_number"],
            subexercises = dictionary["subexercises"],
            download_files = dictionary["download_files"],
            exercise_type = dictionary["exercise_type"]
        )


# might not be needed ###########
def upload_exercises():
    file_name = "exercises.json"
    exercises_out = []
    with open(file_name, "r") as exercises_file:
        exercises_dict = json.load(exercises_file)
    for exercise in exercises_dict:
        exercises_out.append(Exercise.exercise_from_dict(exercise))
    return exercises_out

def save_exercises(exercises_list):
    file_name = "exercises.json"
    dict_out = {}
    exercises_dict_list = []
    for exercise in exercises_list:
        exercises_dict_list.append(exercise.exercise_to_dict())
    dict_out["exercises"] = exercises_dict_list
    with open(file_name, "w") as exercises_file:
            return exercises_file.write(json.dumps(dict_out, exercises_file, ensure_ascii=False, indent=4))
    
###############

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
        file_name = "module{}.json".format(self.module_number)
        with open(file_name, "w") as module_file:
            return module_file.write(json.dumps(self.module_to_dict(), ensure_ascii=False, indent=4))

    @staticmethod
    def dict_to_module(dictionary):
        return Module(
            title = dictionary["title"],
            module_number = dictionary["module_number"],
            description = dictionary["description"],
            exercises = [Exercise.exercise_from_dict(exercise) for exercise in dictionary["exercises"]]
        )

    @staticmethod
    def upload_module(module_number):
        file_name = "module{}.json".format(module_number)
        with open(file_name, "r") as module_file:
            return Module.dict_to_module(json.loads(module_file.read()))


def read_modules():
    modules_list = []
    for i in range(1, NUMBER_OF_MODULES+1):
        modules_list.append(Module.upload_module(i))
    return modules_list




#root_user = User("Miha", "Pompe", "mihapompe", "mihapassword", "miha.pompe@test.com", [1,2,3,4], admin=True)
#some_user = User("Some", "User", "someuser", "somepassword", "some.user@test.com")
#exercise1 = Exercise("Variables", ["Write a function that return a sum of two numbers"], ["variables_tester.py", "variables_exercises.py"])
#module1 = Module("Module 1", "Working on variables and arithmetic expressoions", [exercise1])