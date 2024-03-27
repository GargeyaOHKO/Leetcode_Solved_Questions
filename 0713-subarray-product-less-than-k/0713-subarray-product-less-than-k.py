class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        c=0
        l=0
        prod=1
        for r in range(len(nums)):
            prod*=nums[r]
            while l<=r and prod>=k:
                prod=prod//nums[l]
                l+=1
            c+=(r-l+1)    
        return c
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        