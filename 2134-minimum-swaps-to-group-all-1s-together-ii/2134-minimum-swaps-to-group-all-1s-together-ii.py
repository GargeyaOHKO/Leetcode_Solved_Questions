class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        d={0:0,1:0}
        mini=float('inf')
        one=0
        for i in range(n):
            if nums[i]==1:
                one+=1
        if one==0 or one==n:
            return 0

        l,r=0,0
        flag=True
        while r<(n+one):
            if r-l==one:
                flag=False
            if r-l<one and flag:
                d[nums[r%n]]=d.get(nums[r%n],0)+1
                r+=1
            else:
                mini=min(mini,d[0])
                d[nums[l%n]]-=1
                d[nums[r%n]]+=1
                l+=1
                r+=1
        return mini