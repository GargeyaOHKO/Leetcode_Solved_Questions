class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
            elif i<len(nums)-2 and nums[i]==nums[i+2]:
                return nums[i]
            elif i<len(nums)-3 and nums[i]==nums[i+3]:
                return nums[i]
        