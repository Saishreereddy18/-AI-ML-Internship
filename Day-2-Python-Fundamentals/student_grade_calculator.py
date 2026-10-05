print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
sql = float(input("Enter SQL marks: "))

average = (maths + python + sql) / 3

print("\nStudent Name:", name)
print("Average Marks:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
