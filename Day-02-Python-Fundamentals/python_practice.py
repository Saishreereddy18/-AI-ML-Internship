name = "Sai"
age = 21
cgpa = 8.5
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)


name = "Sai"
age = 21
percentage = 85.5
student = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(student))



marks = 95

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


for i in range(1, 6):
        print(i)


count = 1

while count <= 5:
    print(count)
    count = count + 1


def greet(name):
    print("Hello", name)

greet("Sai")
