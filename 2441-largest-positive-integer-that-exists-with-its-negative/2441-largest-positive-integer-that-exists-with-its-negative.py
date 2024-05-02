class Solution(object):
    def findMaxK(self, nums):
        d={}
        num=-1
        for i in range(len(nums)):
            if abs(nums[i]) not in d:
                d[abs(nums[i])]=[nums[i]]
            else:
                if nums[i] not in d[abs(nums[i])]:
                    if abs(nums[i])>num:
                        num=abs(nums[i])
        return num           
        """
        :type nums: List[int]
        :rtype: int
        """
        