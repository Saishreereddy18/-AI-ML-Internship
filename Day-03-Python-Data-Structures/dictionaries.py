# Python Dictionaries

student = {
    "name": "Sai",
    "age": 21,
    "branch": "CSE",
    "cgpa": 8.5
}

# Print complete dictionary
print(student)

# Accessing values
print(student["name"])
print(student["branch"])
print(student["cgpa"])

# Adding a new item
student["college"] = "Vaagdevi College of Engineering"

print(student)

# Updating a value
student["cgpa"] = 8.6

print(student)

# Removing an item
student.pop("age")

print(student)