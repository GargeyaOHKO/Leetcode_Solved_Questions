class Solution(object):
    def majorityElement(self, nums):
        curr=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=curr:
                count-=1
            else:
                count+=1
            if count<0:
                curr=nums[i]
                count=1
        return curr
        """
        :type nums: List[int]
        :rtype: int
        """
        