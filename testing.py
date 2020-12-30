from model import *

root_user = User("Miha", "Pompe", "mihapompe", "mihapassword", "miha.pompe@test.com", [1,2,3,4], admin=True)
some_user = User("Some", "User", "someuser", "somepassword", "some.user@test.com")


#exercise1 = Exercise("Variables", exercise_number=1, subexercises=["Write a function that return a sum of two numbers"], download_files=["variables_tester.py", "variables_exercises.py"])
#module1 = Module("Module 1", module_number = 1, description = "Working on variables and arithmetic expressoions", exercises=[exercise1])


#module1.save_module()

#module2 = Module.upload_module(1)
#print(module2.title)

print(read_modules())