class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        k=-1
        l=len(nums)
        for i in range(l):
            if(nums[i]!=i):
                return i
                break    
        return i+1              
        """
        :type nums: List[int]
        :rtype: int
        """
        