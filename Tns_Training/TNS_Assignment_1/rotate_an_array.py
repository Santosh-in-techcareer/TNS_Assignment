# 6. Rotate an Array 
# Write a program to rotate an array to the right by K positions. 
# Input: 
# Array: [1, 2, 3, 4, 5] 
# K = 2 
# Output: 
# [4, 5, 1, 2, 3] 
arr = [1, 2, 3, 4, 5] 
k = 2
san = arr[k+1:]
sath = arr[:k+1]
san.extend(sath)
print(san)
