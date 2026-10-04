# 4. Remove Duplicate Elements 
# Write a program to remove duplicate elements from an array. 
# Input: 
# [10, 20, 10, 30, 20, 40, 30] 
# Output: 
# [10, 20, 30, 40] 
arr = [10, 20, 10, 30, 20, 40, 30] 
san = list(dict.fromkeys(arr))
print(san)
