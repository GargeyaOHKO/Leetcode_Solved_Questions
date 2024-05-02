class Solution(object):
    def findMaxK(self, nums):
        s=set()
        num=-1
        for i in range(len(nums)):
            if 0-nums[i] not in s:
                s.add(nums[i])
            else:
                if abs(nums[i])>num:
                    num=abs(nums[i])
        return num           
        """
        :type nums: List[int]
        :rtype: int
        """
        