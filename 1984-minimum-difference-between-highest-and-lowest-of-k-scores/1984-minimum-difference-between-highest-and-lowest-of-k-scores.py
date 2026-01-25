class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        if k>len(nums):
            return nums[0]-nums[-1]
        #print(nums)
        m=float('inf')
        for i in range(len(nums)-k+1):
            m=min(m,nums[i+k-1]-nums[i])
        return m
        