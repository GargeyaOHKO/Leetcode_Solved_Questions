class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0     
        for i in range(len(nums)):
            if nums[i]==0:
                j=i
                while nums[j]==0 and j<len(nums)-1:
                    j+=1
                nums[j],nums[i]=nums[i],nums[j]               
        return nums              
        