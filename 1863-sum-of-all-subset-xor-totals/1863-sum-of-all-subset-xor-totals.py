class Solution(object):
    def subsetXORSum(self, nums):
        s=0
        flag=False
        for i in range((2**len(nums))):
            temps=0
            for j in range(len(nums)):
                if (i&(1<<j))!=0 and flag==False:
                    temps=nums[j]
                    flag=True
                elif (i&(1<<j))!=0 and flag==True:
                    temps^=nums[j]
            s+=temps   
        return s                
        """
        :type nums: List[int]
        :rtype: int
        """
        