# 7. Find the Most Frequent Element 
# Write a program to find the element that occurs the maximum number of times in an array. 
# Input: 
# [2, 5, 2, 8, 5, 2, 3, 5, 2] 
# Output: 
# Most Frequent Element: 2 
# Frequency: 4 
arr = [2, 5, 2, 8, 5, 2, 3, 5, 2] 
sath = sorted(arr)
san = list(dict.fromkeys(sath))
raj = []
for i in sath:
    c = arr.count(i)
    raj.append(c)
b = max(raj)
ci = raj.index(b)
d = san[ci]
print("Frequent of element is :",b)
print("The most occuring element",d)
    

