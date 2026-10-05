import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Charan", "Divya", "Elena", "Fathima", "Gokul", "Hari"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE", "IT", "CSE"],
    "Marks": [85, 72, 91, 68, 78, 88, 65, 95],
    "Attendance": [90, 75, 85, 92, 78, 88, 70, 95]
}

df = pd.DataFrame(data)

print("First 5 students:")
print(df.head())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nStudents scoring more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents with attendance below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted by marks:")
print(df.sort_values("Marks"))