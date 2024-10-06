class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s=sum(nums)
        if s%p==0:
            return 0
        d={0:-1}
        tar=s%p
        s=0
        minlen=float('inf')
        for i in range(len(nums)):
            s=(s+nums[i])%p
            rem=(s-tar+p)%p
            if rem in d:
                minlen=min(minlen,i-d[rem])
            d[s]=i
        
        if minlen==float('inf') or minlen==len(nums):
            return -1
        else:
            return minlen
        
        
        
        