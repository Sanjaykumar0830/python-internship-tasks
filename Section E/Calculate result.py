def calculate_result(student):
    total = sum(student["marks"])
    average = total / len(student["marks"])
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, average, grade

name = input("Enter student name: ")
marks = []
for i in range(1, 4):
    mark = int(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

student = {
    "name": name,
    "marks": marks
}
total, average, grade = calculate_result(student)
print(f"\nStudent Name: {student['name']}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
