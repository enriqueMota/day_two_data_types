"""Data types on python"""

# String with manipulation
print("Hello world!"[-1])


# Numbers in python
# Integer
print(123)

# Float
print(3.14159)

# Boolean
# the "==" operator asks a question instead of asigning the value
print(True == False)


""" Converting data types to other types """

num_char = len(input("What is your name? "))

# You cannot concatenate strings and integers
# for that we use the str function
new_num_char = str(num_char)
print("Your name is " + new_num_char + " characters long")

# The function type gives us the data type of a variable
a = float(123)
print(type(a))


""" CODE CHALLENGE #1"""
""" Printing the sum of a two digit number from an input """\

# Capturing the numbers
two_digit_number = input("Type a two digit number: ")

# Converting the strings to integers
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# printing the sum of the two digit numbers
print(first_digit+second_digit)


""" Math operators """
# Sum
3 + 5

# Substraction
5 - 3

# Multiplication
3 * 2

# Division returns a float
6 / 3

# Power exponent e.g. 2^2
2 ** 2

# PEMDAS
# P->E->M->D->A->S -> order for python math operations
# (P)arenthesis
# (E)xponential exponent
# (M)ultiplication
# (D)ivision
# (A)ddition
# (S)ubtraction
# Multiplication and division have the same order, however the
#  most left operation goes first

print(3 * 3 + 3 / 3 - 3)  # Prints 7

print(3 * (3 + 3) / 3 - 3)  # Prints 3


""" CODE CHALLENGE #2 """
""" Calculate the BMI of the user and return an integer """
""" The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m) """

# Reading the user's height
height = input("enter your height in m: ")
# Reading the user's weight
weight = input("enter your weight kg: ")

# Calculating the BMI by getting the square of the height first
bmi = float(weight) / float(height) ** 2

# Printing the BMI as an integer
print(int(bmi))


""" Number functions """

# Rounds the result to an integer
print(round(8 / 3))

# Rounds the result to however decimal places you specify
print(round(8 / 3, 2))

# Floor division, lowers the number to it's closest integer
print(8 // 3)


result = 4 / 2
result /= 2  # Divides the result by the specified number
result += 2  # Adds the result the specified number
result -= 2  # Subtracts the result the specified number
result *= 2  # Times the result the specified number
print(result)

# Formatted strings
# Converts all data types into a string under the hood
print(f"The result is: {result}")


""" CODE CHALLENGE #3 """
""" Calculate your remaining years, days, weeks, and months assuming you'll live until 90 """

# Reading the age value and parsing it into an integer
age = int(input("What is your current age? "))
# Calculating years
remaining_years = 90 - int(age)
# Calculating days
remaining_days = remaining_years * 365
# Calculating weeks
remaining_weeks = remaining_years * 52
# Calculating months
remaining_months = remaining_years * 12

print(
    f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")


""" DAY TWO PROJECT """
""" Build a bill calculator with the ability of adding a tip """
bill = float(input("What was the total bill? $"))
percentage_tip = int(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)
people_count = int(input("How many people to split the bill? "))
result = round((bill / people_count) * (1 + (percentage_tip / 100)), 2)
print(f"Each person should pay: {result}")
