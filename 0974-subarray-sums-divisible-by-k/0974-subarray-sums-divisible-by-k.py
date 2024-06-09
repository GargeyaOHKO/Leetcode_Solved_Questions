class Solution(object):
    def subarraysDivByK(self, nums, k):
        d={0:1}
        c=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in d:
                d[s%k]=1 
            else:
                c+=d[s%k]
                d[s%k]+=1
                
        return c            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        