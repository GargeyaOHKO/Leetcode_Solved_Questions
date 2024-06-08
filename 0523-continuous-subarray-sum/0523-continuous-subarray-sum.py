class Solution(object):
    def checkSubarraySum(self, nums, k):
        d={0:-1}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if i==0:
                d[s%k]=i
            elif s%k not in d: 
                d[s%k]=i
            elif (i-d[s%k]>1):
                return True              
        return False            
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        