class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)-1,-1,-1):
            rev=int(str(nums[i])[::-1])
            if rev in d:
                d[rev].append(i)
            if nums[i] not in d or len(d[nums[i]])==1:
                d[nums[i]]=[i]
        #print(d)
        mini=float('inf')
        for i in d:
            for j in range(len(d[i])-1):
                if d[i][j]!=d[i][j+1]:
                    mini=min(mini,abs(d[i][j+1]-d[i][j]))
        if mini==float('inf'):
            return -1
        return mini

