class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        d={}
        c,count=0,0
        for i in range(len(nums)):
            c+=nums[i]
            if c==goal:
                count+=1           
            if c-goal in d:
                count+=d[c-goal]
            if c not in d:
                d[c]=1
            else:
                d[c]+=1         
        return count                          
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """