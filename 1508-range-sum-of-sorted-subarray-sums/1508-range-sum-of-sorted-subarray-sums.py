class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                l.append(s)
        l.sort()
        res=0
        for i in range(left-1,right):
            res+=l[i]
        return res%(10**9+7)