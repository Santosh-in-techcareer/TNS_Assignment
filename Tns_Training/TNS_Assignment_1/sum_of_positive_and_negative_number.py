# 3. Sum of Positive and Negative Numbers 
# Write a program to find the separate sum of positive and negative numbers in an array. 
# Input: 
# [10, -5, 20, -8, 15, -2] 
# Output: 
# Positive Sum: 45 
# Negative Sum: -15
arr =[10, -5, 20, -8, 15, -2]
a = 0
b = 0
for i in arr:
    if i>0:
        a = i+a
    else:
        b=i+b
print("Positive Sum:",a)
print("Negative Sum:",b)

