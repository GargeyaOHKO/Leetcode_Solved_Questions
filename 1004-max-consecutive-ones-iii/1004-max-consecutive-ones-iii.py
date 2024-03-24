class Solution(object):
    def longestOnes(self, nums, k):
        d={0:0,1:0}
        l=0
        maxc=0
        for r in range(len(nums)):
            d[nums[r]]+=1         
            while d[0]>k:
                d[nums[l]]-=1
                l+=1                
            maxc=max(maxc,r-l+1)    
        return maxc
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        