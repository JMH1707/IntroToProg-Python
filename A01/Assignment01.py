# ------------------------------------------------------------------------------------------ #
# Title: Assignment 01
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, When, What)
#   J Huminski , 10/13/2024, Created Script
# ------------------------------------------------------------------------------------------ #

COURSE_NAME = "Python 100"

print("Greetings student and welcome to the " + COURSE_NAME + " Class!")
print("Please enter your first and last name to ensure")
print("you are accruately registered with the course.")

print("\n")

student_first_name = input("Please enter your first name: ") # Requests the user's first name
student_last_name = input("Please enter your last name: ") # Requests the user's last name

print("\n")

print(student_first_name + " " + student_last_name + " is registered for " + COURSE_NAME) # Indicates the student has successfully registered 

print("\n")

print(student_first_name + " " + student_last_name + " is registered for " \
      + COURSE_NAME) # Indicates the student has successfully registered
