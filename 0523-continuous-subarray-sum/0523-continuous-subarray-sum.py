class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums)<2:
            return False
        d={0:-1}
        s=0
        for i in range(len(nums)):
            #print(d)
            s+=nums[i]
            if i==0:
                d[s%k]=i
            elif s%k not in d: 
                d[s%k]=i
            elif (i-d[s%k]>1) or s%k==0:
                return True              
        return False            
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        