class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=nums[0]
        for i in range(len(nums)):
            #print(i,maxi,nums[i]+i)
            if maxi>=i:
                maxi=max(maxi,nums[i]+i)
            else:
                return False
            if maxi>=len(nums):
                return True
        return True
