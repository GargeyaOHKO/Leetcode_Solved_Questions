class Solution(object):
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                return abs(nums[i])
            else:    
                nums[abs(nums[i])-1]=0-nums[abs(nums[i])-1]                      
        """
        :type nums: List[int]
        :rtype: int
        """
        