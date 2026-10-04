# #2. Count Even, Odd and Zero 
# Write a program to count the number of even numbers, odd numbers, and zeros in an array. 
# Input: 
# [10, 5, 0, 7, 8, 0, 13, 4] 
# Output: 
# Even: 3 
# Odd: 3 
# Zero: 2
arr = [10, 5, 0, 7, 8, 0, 13, 4] 
a = 0 
b = 0
zero =0
for i in arr:
    if i ==0:
        zero = zero+1
    elif i%2==0:
        a = a+1
    else:
        b= b+1
print("Even:", a)
print("odd:", b)
print("Zero:", zero)

