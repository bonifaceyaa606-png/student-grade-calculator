print("STUDENT GRADE CALCULATOR")

name = input("Enter your name: ")

mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))

average = (mark1 + mark2 + mark3) / 3

print("\nStudent:", name)
print("Average:", average)

if average >= 70:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")