# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables,
#         operators, formatting, and files
# and calculations
# Change Log: (Who, When, What)
#   JHuminski,10/22/2024, Created script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
COURSE_NAME: str = "Python 100"
COURSE_PRICE: float = 999.98
STATE_TAX: float = .09
TOTAL_PRICE: float = COURSE_PRICE + COURSE_PRICE * STATE_TAX
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
file_obj = None
file_reference = open(FILE_NAME, "w")

# Get data from the user
student_first_name = input("Please enter your first name: ")
student_last_name = input("Please enter your last name: ")

# Present the data to the user
csv_data = f"{student_first_name},{student_last_name},{COURSE_NAME},{COURSE_PRICE},{TOTAL_PRICE:.2f}"

message = (
    f"\nThank you, {student_first_name} {student_last_name}.\n" 
    f"You have signed up for {COURSE_NAME}.\n"
    f"The cost of the course is {COURSE_PRICE}.\n"
    f"Your total with tax is: {TOTAL_PRICE:.2f} "
)

print(message, "\n")
print("CSV DATA:", csv_data)

# Process the data to a file
file_reference.write(csv_data)
file_reference.close()
print("\nYour data has been successfully recorded!")
