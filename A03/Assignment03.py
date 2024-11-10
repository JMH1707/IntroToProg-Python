# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   J. Huminski, 10/27/2024, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = ("----Course Registration Program----\n\n"
             "Select from the following menu:\n\n"
             "1. Register a student for the course\n"
             "2. Show current data\n"
             "3. Sava data to a file\n"
             "4. Exit the program"
             "\n-----------------------------------------\n")
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj = None
menu_choice: str = ""

# Present the menu of choices
while True:
    print(MENU) # This prints the menu of options to display to the user.

# Input user data
    menu_choice = input("Please enter a menu option from the list above: ")
    match menu_choice:
        case "1":
            print("Please enter the following information to "
                  "register a new student.\n") # Instructs user what info is needed
            student_first_name = input("Please enter the student's first name: ") # Requests first name
            student_last_name = input("Please enter the student's last name: ") # Requests last name
            course_name = input("Please enter the course name you wish to register for: ") # Requests course name

            print(f"\nCongratulations, {student_first_name} {student_last_name} "
                  f"has successfully registered for {course_name}!\n") # Success message
            continue
# Present the current data
        case "2":
            if not student_first_name or not student_last_name or not course_name: # Check if variables hold data.
                print("You have not input valid data. "
                      "Please select Option 1 to input your data.\n") # Print message to go back and enter data.
            else:
                csv_data = f"\n{student_first_name},{student_last_name},{course_name}\n"
                print(csv_data) # Prints the formatted CSV data
                continue

# Save the data to a file
        case "3":
            if not student_first_name or not student_last_name or not course_name: # Check if variables hold data.
                print("You have not input valid data. "
                      "Please select Option 1 to input your data.\n") # Print message to go back and enter data
            else:
                file_obj = open(FILE_NAME, "w") # Opens the constant FILE_NAME
                file_obj.write(csv_data) # Writes the CSV data to the file
                file_obj.close() # Closes and saves the CSV file
                print("\nYour request has been processed and saved.\n") # Success message!
                continue

# Stop the loop
        case "4":
            print("\nYou have exited the program") # Informs the user they've exited the program.
            break

# Correcting the user option:
        case _: # Ensures user is entering a proper menu option.
            print("\nInvalid option. Please read the menu "
                  "and choose an applicable option.\n") # Informs user their option is wrong.
            continue
