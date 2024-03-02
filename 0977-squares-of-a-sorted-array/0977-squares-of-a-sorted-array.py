class Solution(object):
    def sortedSquares(self, nums):
        mini=min(nums)
        maxi=max(nums)
        l=[0]*(max(abs(mini),abs(maxi))+1)
        lf=[]
        for i in nums:
            l[abs(i)]+=1
        for i in range(len(l)):
            if l[i]>0:                
                lf=lf+([i**2]*l[i])
        return lf
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        