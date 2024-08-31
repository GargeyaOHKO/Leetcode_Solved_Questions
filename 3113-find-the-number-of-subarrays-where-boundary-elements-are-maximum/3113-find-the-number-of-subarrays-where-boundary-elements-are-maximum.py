class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        d={}
        c=0
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            c+=d[i]
            c+=(d[i]*(d[i]-1))//2
        return c
