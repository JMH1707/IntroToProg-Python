# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
# Jesse Huminski, 11/04/2024, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
----Course Registration Program-----
Select from the following menu:
1. Register a student for a course
2. Show current data
3. Save data to file
4. Exit the program
-------------------------------------\n'''

FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: list = []
students: list = []
message: str = ""

# Present and Process the data
file = open(FILE_NAME, "r")
for each_row in file.readlines(): # Read data from all rows in the file
    student_data = each_row.split(",") # Splits each row at the comma
    student_data = [student_data[0],student_data[1],student_data[2].strip()] # assigns data to the variable
    students.append(student_data) # Creates a list of lists for the data
file.close()

message = ("\n\nHello, student! Welcome to the Course Enrollment Program.\n"
           "Please select an option from the menu below to get started\n"
           "enrolling in a course.")
print("-"*50)
print(message) # Prints welcome message

# Present the menu of choices
while True:
    print(MENU)
    menu_choice = input("Please enter your selection from the menu above: ")
    match menu_choice:

    # Input user data
        case "1":
            student_first_name = input("What is the student's first name? ")
            student_last_name = input("What is the student's last name? ")
            course_name = input("What course would you like to enroll the student in? ")
            message = (f"\nThank you, {student_first_name} {student_last_name}. You have successfully registered"
                       f" for {course_name}")
            students.append([student_first_name, student_last_name, course_name])
            print(message)

    # Present the current data
        case "2":
            print("\n")
            print("-" * 55)
            print(f"| {'First Name':^10} | {'Last Name':^10} | {'Course':^25} |")
            print("-" * 55)
            for student_data in students:
                print(f"| {student_data[0]:^10} | {student_data[1]:^10} | {student_data[2]:^25} |")
                print("-" * 55)


    # Save the data to a file
        case "3":
            csv_data = f"{student_first_name}, {student_last_name}, {course_name}\n"
            file = open(FILE_NAME, "a")
            file.write(csv_data)
            file.close()
            print("\nYour data has successfully been saved!\n")


    # Stop the loop
        case "4":
            print("Program Ended")
            break

    # Require a correct menu choice
        case _:
            print("\nINVALID CHOICE\nPlease select a correct option.")
