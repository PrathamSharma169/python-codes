class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i]
s=[1,2,3,2]
cl=Solution()
print(cl.findDuplicate(s))