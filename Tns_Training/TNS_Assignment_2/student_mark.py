import matplotlib.pyplot as plt

students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

marks = [85, 72, 91, 45, 67, 88, 35, 76, 55, 93]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

excellent = sum(80 <= mark <= 100 for mark in marks)
good = sum(60 <= mark <= 79 for mark in marks)
average = sum(40 <= mark <= 59 for mark in marks)
needs_improvement = sum(mark < 40 for mark in marks)

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
values = [excellent, good, average, needs_improvement]

plt.pie(values, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")
plt.show()
