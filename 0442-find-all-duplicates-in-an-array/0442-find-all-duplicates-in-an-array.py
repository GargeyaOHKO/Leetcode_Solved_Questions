class Solution(object):
    def findDuplicates(self, nums):
        l=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                l.append(abs(nums[i]))
            nums[abs(nums[i])-1]=0-nums[abs(nums[i])-1]
        return l    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        