class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum=[0 for _ in range(len(nums))]
        rsum=[0 for _ in range(len(nums))]
        l,r=0,0
        for i in range(len(nums)):
            l+=nums[i]
            r+=nums[-1-i]
            lsum[i]=l
            rsum[-1-i]=r
        res=[]
        for i in range(len(lsum)):
            res.append(abs(lsum[i]-rsum[i]))
        return res

