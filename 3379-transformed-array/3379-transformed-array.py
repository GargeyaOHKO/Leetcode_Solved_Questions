class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        temp=nums[:]
        n=len(nums)
        for i in range(n):
            nums.append(nums[i])
        for i in nums:
            temp.append(i)
        nums=temp[:]
        res=[0 for i in range(n)]
        for i in range(n,len(nums)-n):
            if nums[i]==0:
                res[i-n]=0
            elif nums[i]<0:
                res[i-n]=nums[(i-abs(nums[i])%n)]
            else:
                res[i-n]=nums[(i+nums[i]%n)]
        return res
