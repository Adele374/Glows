# Simple Student ID Generator
# CS27 Group Project - Part 1

print("=====================================")
print("        STUDENT ID GENERATOR         ")
print("=====================================\n")

# ---- INPUTS ---- #
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
school = input("Enter your school name: ")
department = input("Enter your department: ")
level = int(input("Enter your academic level (1, 2, 3...): "))
student_id = input("Enter your student ID number: ")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

email = input("Enter your school email: ")
registered_text = input("Are you registered? (yes/no): ")

# BOOL variable
is_registered = (registered_text == "yes")

# ---- SIMPLE CALCULATIONS ---- #
age_next_year = age + 1
total_weight_height = weight + height
year_created = 2025
years_at_school = level - 1

# ---- OUTPUT ---- #
print("\n=====================================")
print("           STUDENT SUMMARY           ")
print("=====================================")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Next year you will be: {age_next_year} years old")
print(f"School: {school}")
print(f"Department: {department}")
print(f"Level: {level}")
print(f"Student ID: {student_id}")
print(f"Email: {email}")
print(f"Registered: {is_registered}")

print("-------------------------------------")
print(f"Height: {height} m")
print(f"Weight: {weight} kg")
print(f"Height + Weight = {total_weight_height}")

print("-------------------------------------")
print(f"ID card created in: {year_created}")
print(f"Years already spent at school: {years_at_school}")
print("=====================================")

print("        END OF STUDENT PROFILE       ")
print("=====================================")