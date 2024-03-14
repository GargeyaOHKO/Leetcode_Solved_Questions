class Solution(object):
    def isPossibleToSplit(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>2:
                return False
        return True                
        """
        :type nums: List[int]
        :rtype: bool
        """
        