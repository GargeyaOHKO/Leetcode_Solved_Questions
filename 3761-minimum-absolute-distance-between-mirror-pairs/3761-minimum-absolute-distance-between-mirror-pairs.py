class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d={}
        mini=float('inf')
        for i in range(len(nums)-1,-1,-1):
            rev=int(str(nums[i])[::-1])
            if rev in d:
                mini=min(mini,d[rev][0]-i)
                d[rev].append(i)
            if nums[i] not in d or len(d[nums[i]])==1:
                d[nums[i]]=[i]
        if mini==float('inf'):
            return -1
        return mini

