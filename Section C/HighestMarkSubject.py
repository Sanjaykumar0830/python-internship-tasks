marks = {
    "Maths": 88,
    "Science": 92,
    "English": 85,
    "History": 78,
    "Computer": 95
}

highest_subject = max(marks, key=marks.get)
print("Marks:", marks)
print("Subject with highest marks:", highest_subject, "=>", marks[highest_subject])
