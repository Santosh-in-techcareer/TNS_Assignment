# 9. Check Whether Two Arrays are Equal 
# Given two arrays, check whether they contain the same elements with the same frequency, 
# regardless of their order. 
# Input: 
# Array 1: [1, 2, 2, 3, 4] 
# Array 2: [4, 2, 1, 2, 3] 
# Output: 
# Arrays are Equal 
Array1 =[1, 2, 2, 3, 4] 
Array2 =[4, 2, 1, 2, 3] 
sath = sorted(Array1)
raj = sorted(Array2)
if sath ==raj :
    print("Arrays are Equal")