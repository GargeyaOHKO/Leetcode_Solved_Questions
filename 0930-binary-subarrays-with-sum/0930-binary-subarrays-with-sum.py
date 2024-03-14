class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def helper(goal):
            if goal<0:
                return 0
            l,count=0,0    
            c=0
            for i in range(len(nums)):
                c+=nums[i]
                while c>goal:
                    c-=nums[l]
                    l+=1
                count+=(i-l+1)    
            return count
        return helper(goal)-helper(goal-1)        
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """