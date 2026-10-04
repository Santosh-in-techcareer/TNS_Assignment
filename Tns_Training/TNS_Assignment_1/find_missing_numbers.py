# 5. Find the Missing Number 
# An array contains numbers from 1 to N, but one number is missing. Find the missing number. 
# Input: 
# [1, 2, 3, 5, 6, 7] 
# Output: 
# Missing Number: 4 
arr = [1, 2, 3, 5, 6, 7] 
a = 1
b = 0
for i in arr:
    if i ==a:
        a=a+1
    else:
        b=a
print(b)

        
