# Python File Handling

# Writing to a file
with open("students.txt", "w") as file:
    file.write("Sai, CSE, 8.5\n")
    file.write("Ravi, ECE, 8.2\n")
    file.write("Anu, IT, 9.0\n")

print("Data written successfully!")


# Reading from a file
with open("students.txt", "r") as file:
    data = file.read()

print("\nStudent Records:")
print(data)