# Student Marks Analysis 
# • Create a NumPy array containing the marks of 10 students. 
# • Find the total marks. 
# • Find the average marks. 
# • Find the highest and lowest marks. 
# • Display the marks greater than 75. 
import numpy as np

marks = np.array([85, 72, 90, 68, 76, 95, 81, 64, 88, 79])

total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
greater_than_75 = marks[marks > 75]

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Marks greater than 75:", greater_than_75)










#age and salary are feature and prudiction is target variable(c)
#b
#c
#b
#B
#A
#B
#B
#D
#d