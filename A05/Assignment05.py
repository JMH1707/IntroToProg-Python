# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   J. Huminski, 11/11/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json


# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = """----Course Registration Program----
Select an option from the following menu:
    1. Register a student for a course
    2. Show current data
    3. Save data to file
    4. Exit program
    """

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file = None
menu_choice: str = ""
message: str = ""
student_data: dict = {}
students: list = []


# When the program starts, read the file data into a list of lists (table)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file) # Extract the data from the file
    file.close()
except FileNotFoundError as e:
    print("ERROR: JSON file does not exist.")
    print("-- Technical Information --")
    print(e, e.__doc__, type(e), sep = '\n')
    print("The program has ended because an error was encountered")
    exit()
except Exception as e:
    print("A non-specific error has occurred")
    print ("-- Technical Information --")
    print (e, e.__doc__, type(e), sep = '\n')
    print("The program has ended because an error was encountered")
    exit()

# Present and Process the data
while True: # Start the loop

    # Present the menu of choices
    print("-" * 50)
    print(MENU)
    print("-" * 50)
    print("\n")
    menu_choice = input("Please enter your selection from the menu above: ")
    match menu_choice:

    # Input user data
        case "1":
            while True: # Nested while loop to repeat if error occurs.
                try:
                    student_first_name = input("Please enter your first name: ")
                    if not student_first_name.isalpha():
                        raise ValueError("First name cannot contain numeric value")
                    break # Will only break if ValueError is not raised
                except ValueError as e:
                    print(e)
                    print("\n")
                except Exception as e:
                    print("A non-specific error has occurred")
                    print("-- Technical Information --")
                    print(e, e.__doc__, type(e), sep='\n')

            while True: # Nested while loop to repeat if error occurs.
                try:
                    student_last_name = input("Please enter your last name: ")
                    if not student_last_name.isalpha():
                        raise ValueError("Last name cannot contain numeric value")
                    break # Will only break if ValueError is not raised
                except ValueError as e:
                    print(e)
                    print("\n")
                except Exception as e:
                    print("A non-specific error has occurred")
                    print("-- Technical Information --")
                    print(e, e.__doc__, type(e), sep='\n')

            course_name = input("Please enter the course you wish to enroll in: ")

            message = (f"\nThank you {student_first_name} {student_last_name}."
                        f" You have successfully enrolled in {course_name}")

            print(message)

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}

            students.append(student_data)
            continue


    # Present the current data
        case "2":
            try:
                print("\n")
                print("-" * 50)
                for student in students:
                # Process the data to create and display a custom message
                    message = (f"Student {student['FirstName']} {student['LastName']} "
                           f"has been enrolled in {student['CourseName']}.")
                    print("-" * 50)
                    print(message)
            except FileNotFoundError as e:
                print("ERROR: JSON file does not exist.")
                print("-- Technical Information --")
                print(e, e.__doc__, type(e), sep='\n')
                print("The program has ended because an error was encountered")
                exit()
            except Exception as e:
                print("A non-specific error has occurred")
                print("-- Technical Information --")
                print(e, e.__doc__, type(e), sep='\n')
                print("The program has ended because an error was encountered")
                exit()
            continue

    # Save the data to a file
        case "3":
            try:
                print("\n")
                print("Your data has successfully been saved to", FILE_NAME, "!")
                file = open(FILE_NAME, "w")
                json.dump(students, file, indent=4)
                file.close()

            except FileNotFoundError as e:
                print("-- Technical Information --")
                print(e, e.__doc__, type(e), sep='\n')
                print("The program has ended because an error was encountered")
                exit()
            except Exception as e:
                print("A non-specific error has occurred")
                print("-- Technical Information --")
                print(e, e.__doc__, type(e), sep='\n')
                print("The program has ended because an error was encountered")
                exit()
            continue


    # Stop the loop
        case "4":
            print("You have exited the program!")
            break

        case _:
            print("\nPlease select an appropriate menu option\n")