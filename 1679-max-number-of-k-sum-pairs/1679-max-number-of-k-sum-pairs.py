class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l,r=0,len(nums)-1
        c=0
        while l<r:
            if nums[l]+nums[r]==k:
                c+=1
                l+=1
                r-=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1
        return c              
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        