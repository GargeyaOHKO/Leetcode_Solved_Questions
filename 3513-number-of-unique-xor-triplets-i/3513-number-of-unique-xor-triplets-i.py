class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        n=1
        while n<=len(nums):
            n*=2
        return n