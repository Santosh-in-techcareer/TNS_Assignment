#find the second largest number 
#find an element in array
class Solution:
    @staticmethod
    def second_element(arr):
        s = len(arr)
        for i in range(2):
            for j in range(0,s-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr[s-2]
        
        

arr = [11,2,3,4,5,6,7,8,10,9]

c = Solution.second_element(arr)
print(c)