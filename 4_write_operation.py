# there are 2 mode to open and modify the file
# 1. write mode (w)
# 2. append mode (a)

# design a script to write user's record to a file
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

with open("user_record.txt", "x") as file:
    file.write(f"First Name: {first_name}, Last Name: {last_name}\n")
