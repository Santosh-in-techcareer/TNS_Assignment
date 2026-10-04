class Solution:
    @staticmethod
    def san(target,sa):
        s = len(sa)
        for i in range(s):
            if sa[i]==target:
                return sa[i]


sa = [1,2,3,4,5,6,7,8,9,10]
target = 10
c = Solution.san(target,sa)
print(c)