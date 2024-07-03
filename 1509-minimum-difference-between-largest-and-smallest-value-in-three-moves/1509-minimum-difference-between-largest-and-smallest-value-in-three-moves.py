class Solution(object):
    def minDifference(self, nums):
        n=len(nums)
        if len(nums)<=4:
            return 0
        nums.sort()
        l,r=0,n-4
        mini=float('inf')
        dif=r-l
        for i in range(n-dif):
            print(l,r)
            mini=min(mini,nums[r]-nums[l])
            l+=1
            r+=1
        return mini
        """
        :type nums: List[int]
        :rtype: int
        """
        