# CodeSite
Website for learning and testing Python.

## User mode
To enter the site a user must enter it's credentials (username and password). He can optionally opt out of saving their login. The main page is the modules page, where the user can see all the modules available to them. A new module is made available to them every week. Progress of the entire program or module can be seen on the right side. Inside every module the user can see different exercises, their descriptions and some examples. The download files button will download all the necessary Python files (<name_of_exercise>_exercise.py and <name_of_exercise>_tester.py). Exercises are solved in the _exercise.py file and to test them against test cases you run _tester.py. The tester file will evaluate the user's code and send the final score back to this website.

## Admin mode
Admin is a normal user and has the same features, but also a few additional ones. In this mode you can:
* See all user data (except passwords) and their progress
* Add users
* Add new exercises and test files
* Access to templates

## Requirements
Before you begin, ensure you have met the following requirements:
* You have Python 3 and packages Bottle and Json installed.
* To run tested files you should also install Numpy.

## How to install and run this project
* Clone the repository to your desired location.
* Run the file controller.py using by running `python controller.py`
* In your browser open [localhost:8080/login](localhost:8080/login)

## Features
* Login page, remember me checkbox, password hidden
* Passwords encrypted and saved as SHA256 hashes
* Track your overall progress and progress for an individual module and exercise
* Categorized modules, exercises and parts (subexercises)
* Exercise descriptions can be stylized using HTML tags
* Support for 3 types of exercises (exercise, text, video)
    * Exercise type - custom tester files, progress 
    * Text type - mark as completed button, download files
    * Video type -mp4 video support, video thumbnail, mark as completed button, download files
* Additional webpages: instructions, about, contact me, license and other resources
* Profile view - view all of your personal information that is stored
* Stats view - view your progress, for each module and exercise
* Logout - All cookies will be deleted
* New modules are unlocked every week
* Admin mode
    * Add exercise
    * Add part
    * Add new user
    * Access to templates for _exercise.py and _tester.py files
    * Dashboard - see data and progress of all users


## Resources
* [Bottle documentation](https://bottlepy.org/docs/dev/index.html)
* [Bootstrap examples and documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)