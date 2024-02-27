class Solution(object):
    def missingNumber(self, nums):
        n1=len(nums)
        for i in range(len(nums)):
            n1^=i^nums[i]
        return n1     
        """
        :type nums: List[int]
        :rtype: int
        """
        