class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=0
        nonz=False
        for i in nums:
            x^=i
            if i!=0:
                nonz=True
        if x!=0:
            return len(nums)
        if x==0 and nonz:
            return len(nums)-1
        return 0

