class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        l=[0]*(max(nums)+1)
        for i in nums:
            l[i]+=1
        s=0
        for i in range(len(l)-1):
            if l[i]>1:
                l[i+1]+=l[i]-1
                s+=l[i]-1
        s+=((l[-1]-1)*l[-1])//2
        return s
