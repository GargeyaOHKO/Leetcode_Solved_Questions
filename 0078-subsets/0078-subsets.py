class Solution(object):
    def subsets(self, nums):
        fl=[]
        for i in range(2**len(nums)):
            l=[]
            for j in range(len(nums)):
                if i&(1<<j)!=0:
                    l.append(nums[j])
            fl.append(l)
        return fl            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        