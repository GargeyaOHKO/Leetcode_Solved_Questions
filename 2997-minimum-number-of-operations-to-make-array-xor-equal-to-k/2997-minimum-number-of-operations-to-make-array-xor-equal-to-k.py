class Solution(object):
    def minOperations(self, nums, k):
        ans=nums[0]
        for i in range(1,len(nums)):
            ans^=nums[i]
        c=0
        for i in range(32):
            if (ans & 1<<i)!=(k & 1<<i):
                c+=1
        return c        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        