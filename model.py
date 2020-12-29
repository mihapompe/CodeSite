
NUMBER_OF_MODULES = 4



class User():
    def __init__(self, name, surname, username, password, mail, enabled_modules = [1], progress, admin = False):
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



    
class Module():
    def __init__(self, title, description = "", exercises):
        self.title = title                      # module title
        self.description = description          # module description
        self.exercises = exercises              # list of exercises

class Exercise():
    def __init__(self, title, sub_exercises, download_files, exercise_type = "exercise"):
        self.title = title                      # title of the exercise, e.g. "Loops"
        self.subexercises = subexercises        # list of subexercises, string
        self.download_files = download_files    # list of file names, e.g. loops_tester.py
        self.type = exercise_type               # ["exercise", "text", "video"]


root_user = User("Miha", "Pompe", "mihapompe", "mihapassword", "miha.pompe@test.com", [1,2,3,4], admin=True)
some_user = User("Some", "User", "someuser", "somepassword", "some.user@test.com")


exercise1 = Exercise("Variables", ["Write a function that return a sum of two numbers"], ["variables_tester.py", "variables_exercises.py"])
module1 = Module("Module 1", "Working on variables and arithmetic expressoions", [exercise1])

def read_modules():
