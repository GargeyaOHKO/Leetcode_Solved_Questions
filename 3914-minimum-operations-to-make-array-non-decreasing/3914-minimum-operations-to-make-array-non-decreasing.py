class Solution:
    def minOperations(self, nums: list[int]) -> int:
        add=0
        maxi=nums[0]
        for i in range(1,len(nums)):
            if nums[i]+add<maxi:
                add+=nums[i-1]-nums[i]
            maxi=max(maxi,nums[i]+add)
        return add
