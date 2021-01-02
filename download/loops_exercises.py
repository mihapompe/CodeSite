
# =============================================================================
# Loops
# Loops are something you'll use on a daily basis. Looping though different
# kinds of data is something you have to become very comfortable with. You
# should internalize their working, understand how multiple nested loops 
# interact with your code. These exercises are the first step towards that 
# goal and we'll be using the a lot in the next weeks.
# =============================================================================

# =============================================================================
# Exercise 1
# Write a function that returns the sum of the first n natural numbers.
# Natural numbers are 1, 2, 3, 4, ...
#
#   >>> sum_natural_numbers(4):
#   10
#
# Optional: this exercise can be solved without using for loops and just using
# basic mathematical expressions. If you like you can try to derive a formula
# for the sum of first n numbers.
# =============================================================================

def sum_natural_numbers(n):

    return

# =============================================================================
# Exercise 2
# Write a function that returns the sum of first n raised to the power k.
# For example if n=3 and k=2 the sum should equal sum = 1^2 + 2^2 + 3^2.
#
#   >>> sum_powers(3, 2)
#   14
#
# =============================================================================

def sum_powers(n,k):

    return

# =============================================================================
# Exercise 3
# Write a funciton that returns the sum of all digits in a number.
#
#   >>> sum_digits(1234):
#   10
#
# =============================================================================

def sum_digits(n):

    return

# =============================================================================
# Exercises 4
# Write a function that the return the sum of all digits between numbers n and
# m, including these two.
#
#   >>> sum_digits_between_numbers(8, 11)
#   20
#
# =============================================================================

def sum_digits_between_numbers(n, m):

    return

# =============================================================================
# Exercise 5
# Two numbers a and b are in golden ratio if a/b = (a+b)/a. The golden ratio
# equals to fi = (1+sqrt(5))/2 which is approximately fi = 1.6180339... 
# Since this ratio is irrational (decimals go to infinity) we usually use 
# an approximation. To calculate the approximation we use this formula 
# fi_n+1 = 1 + 1/fi_n where fi_0 = 1. This is a recursive formula starting at
# 0 and the acuracy of the approximation increases with every step. We say
# that when n approaches infinity the formula approaches the real value,
# fi_infinity = fi. Example of calculation: fi_1 = 1 + 1/fi_0 = 1 + 1/1 = 2
# f2 = 1 + 1/fi_1 = 1 + 1/2 = 1.5.
#
# Write a funciton that returns the n-th approximation.
#
#   >>> golden_ratio(2)
#   1.5
#
# =============================================================================

def golden_ratio(n):

    return

# =============================================================================
# Exercise 6
# Help your neighbours kid learn multiplication, but providing him
# a multiplication table up to a given number n. The output shoud be a string,
# where numbers are seperated by a space and each line seperated by \n.
#
#   multiplication_table(4)
#   "1 2 3 4\n2 4 6 8\n3 6 9 12\n4 8 12 16"
#
# If you were to print this you'd get this:
#   1 2 3 4
#   2 4 6 8
#   3 6 9 12
#   4 8 12 16
# Watch that you don't have any excess spaces or new lines.
# =============================================================================

def multiplication_table(n):

    return