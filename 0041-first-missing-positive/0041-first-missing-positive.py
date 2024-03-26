class Solution(object):
    def firstMissingPositive(self, nums):      
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=0:
                nums.pop(i)

        print(nums)
        for i in range(len(nums)):
            print(nums[i])
            if (abs(nums[i])-1)>=len(nums):
                continue
            else:
                if nums[abs(nums[i])-1]>0:
                    nums[abs(nums[i])-1]=0-nums[abs(nums[i])-1]
        print(nums)
        c=1
        for i in nums:
            if i>0:
                return c    
            c+=1        
        return c
        """
        :type nums: List[int]
        :rtype: int
        """
        