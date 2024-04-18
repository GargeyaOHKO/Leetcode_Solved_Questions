class Solution(object):
    def getConcatenation(self, nums):
        l=nums[:]+nums[:]
        return l
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        