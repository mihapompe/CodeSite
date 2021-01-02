
##### WEEK 1 - Numbers, strings, arithmetic operations and conditional statements


##### Exercise 1 #####
# Write a function that calculates the area of a rectangle, which is given
# by the formula A = a * b. The function should be called area(a, b).
#
#   area(4, 3):
#   >>> 12
#
######################

def area(a, b):

    return

##### Exercise 2 #####
# Write a function called mean(a, b) that calculates the mean of the two numbers
#
#   mean(2, 4)
#   >>> 3
#
######################

def mean(a, b):

    return


##### Exercise 3 #####
# Write a function check_for_snakes(word) that check if the word is describing a snake.
# Snake can be described with the following words: snake, python, anaconda, boa.
# If the word is describing a snake return True, otherwise return False
# All the test cases will use words in lower caps
#
#   check_for_snakes("snake")
#   >>> True
#
#   check_for_snakes("tiger")
#   >>> False
#
######################

def check_for_snakes(word):

    return

##### Exercise 4 #####
# Check wether a number is even or odd. The function should be called even(n) and
# should return True if n is even and False otherwise
#
#   even(2)
#   >>> True
#
#   even(3)
#   >>> False
#
######################

def even(n):

    return


##### Exercise 5 #####
# Write a decision tree that will allow you to choose which ice crean to chose based on 
# temperature and your mood.
# -If it is below 0 (degrees Celsius) don't buy one and return None, regardless of your mood.
# -If your are feeling happy or motivated and is less than 10 degrees outside 
#  you'll be craving some strawberry
# -In anger or sadness with less than 10 degrees outside not even ice cream can make you happy, 
#  so you souldn't buy one.
# -When it is above 30, you'll want to get some vanilla as soon as possible no matte what mood.
# -You use blueberry ice cream to calm yourself down (anger) when it is between 10 and 30 degrees.
# -In all other cases just get chocolate
# 
# Write a function called pick_ice_cream(temp, mood) that will return one of the ice cream flavours: 
# strawberry, vanilla, blueberry and chocolate. You can be in one of the following moods: 
# happy, sad, angry, motivated
#
#   pick_ice_cream(15, "happy")
#   >>> "chocolate"
#
#   pick_ice_cream(0, "motivated")
#   >>> None
#
######################

def pick_ice_cream(temp, mood):

    return

##### Exercise 6 #####
# Write a function that tells you if a given year is a leap year or not. A year is a leap year if it is divissable
# by 4, unless it is also divisable by 100 in which case it is not a leap year. In case it is divisable by 400 it is
# again a leap year. Write a function call leap(year) that returns True or False.
#
#   leap(2004)
#   >>> True
#
#   leap(1900)
#   >>> False
#
######################

def leap(year):

    return


##### Exercise 7 #####
# This exercise will test your skills with string manipulation. You will be given a sentace that contains
# a company name (upper case) and its number of employees. Write a function parse(sentance) that will 
# extract the company name and the number of employees. Your function should return a sentance saying 
# "<company_name> is increasing their number of employees to <increased_number_of_employees>", 
# where the second value shoudl be 10 % more than the number of employees from the input. 
# The first word in the sentance will never be the company name.
#
#   parse("Breaking news Apple has now got whoping 200000 employees!")
#   >>> "Apple is increasing their number of employees to 220000"
#
# Use the following two helper functions that allow you to parse out the company name and number of empoyees.
#
# This function will return the company name as string.

def find_company(words):
    for word in words:
        if word[0].isupper() and word != words[0]:
            return word
    return None

#
#   find_company(["LOL", "Google", "has", "100000", "employees"])
#   >>> "Google"
#
# This function will return the number of employees as string

def find_number(words):
    for word in words:
        if word.isdigit():
            return word
    return None

#
#   find_number(["LOL", "Google", "has", "100000", "employees"])
#   >>> "100000"
#
######################

def parse(sentance):

    return



r = requests.post('http://127.0.0.1:8080/exercise_results/mihapompe', data={'module_number': 1, 'exercise_number': 1, 'score': score})