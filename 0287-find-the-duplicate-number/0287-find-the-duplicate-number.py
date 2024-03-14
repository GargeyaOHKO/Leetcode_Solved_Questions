class Solution(object):
    def findDuplicate(self, nums):
        r1=0
        r2=0
        while True:
            r1=nums[r1]
            r2=nums[nums[r2]]
            if r1==r2:
                break
        r3=0
        while True:
            r3=nums[r3]
            r1=nums[r1]
            if r3==r1:
                break
        return r3                
        """
        :type nums: List[int]
        :rtype: int
        """
        