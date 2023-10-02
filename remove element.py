def removeElement(nums, val):
    cnt=len(nums)
    for i in range(len(nums)):
        if nums[i]==val:
            nums[i]=''
            cnt=cnt-1
    nums.sort()
    return cnt
s=[1,2,3,1,4,3]
removeElement(s,1)
print(s)