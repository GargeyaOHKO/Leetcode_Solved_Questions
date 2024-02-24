class Solution(object):
    def missingNumber(self, nums):
        s=set()
        for i in range(max(nums)+2):
            s.add(i)
        for i in nums:
            if(i in s):
                s.remove(i)       
        return s.pop()             
        """
        :type nums: List[int]
        :rtype: int
        """
        