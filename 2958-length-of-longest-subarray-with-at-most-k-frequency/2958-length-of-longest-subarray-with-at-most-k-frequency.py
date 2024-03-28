class Solution(object):
    def maxSubarrayLength(self, nums, k):
        d={}
        l=0
        maxl=0
        for r in range(len(nums)):
            d[nums[r]]=d.get(nums[r],0)+1
            if d[nums[r]]<=k:
                maxl=max(maxl,r-l+1)
            while d[nums[r]]>k:
                d[nums[l]]-=1
                l+=1
        return maxl            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        