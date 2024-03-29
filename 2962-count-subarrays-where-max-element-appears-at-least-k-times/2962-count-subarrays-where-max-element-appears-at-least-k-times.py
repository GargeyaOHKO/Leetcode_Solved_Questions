class Solution(object):
    def countSubarrays(self, nums, k):
        maxnum=max(nums)
        l=0
        d={maxnum:0}
        c=0
        for r in range(len(nums)):
            d[nums[r]]=d.get(nums[r],0)+1
            while d[maxnum]==k:
                c+=(len(nums)-r)
                d[nums[l]]-=1
                l+=1
        return c        


        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        