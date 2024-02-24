class Solution(object):
    def singleNumber(self, nums):
        n=0
        for i in nums:
            n=n^i
        return n    
        """
        :type nums: List[int]
        :rtype: int
        """
        