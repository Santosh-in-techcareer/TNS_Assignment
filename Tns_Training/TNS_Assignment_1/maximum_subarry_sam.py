# 8. Maximum Subarray Sum 
# Write a program to find the maximum sum of a contiguous subarray. 
# Input: 
# [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
# Output: 
# Maximum Subarray Sum: 6 
# Subarray: 
# [4, -1, 2, 1] 
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
san = arr[0]
high = arr[0]
sath = 0
raj = 0 
divya = 0
for i in range(1,len(arr)):
    san= max(arr[i],san +arr[i])
    if san == arr[i]:
        sath = i
    high = max(high,san)
    if high ==san:
        raj = sath
        divya = i
print(high)
print("Subarray:",arr[raj:divya+1])

#kedane alogoritm

#reinforcement learning
#Q-learning
#SARSA
#DEEP Q NETWORK
#MONTE CARLO TREE SEARCH