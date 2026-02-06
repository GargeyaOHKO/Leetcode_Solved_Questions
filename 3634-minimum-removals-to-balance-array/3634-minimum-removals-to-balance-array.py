class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        m=0
        j=0
        for i in range(len(nums)):
            while j<len(nums) and nums[i]*k>=nums[j]:
                j+=1
            m=max(m,j-i)
        return len(nums)-m
