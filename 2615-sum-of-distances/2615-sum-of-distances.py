class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        #print(d)
        dsum={}
        for i in d:
            dsum[i]=[]
            s=0
            for j in range(len(d[i])):
                s+=d[i][j]
                dsum[i].append(s)
        #print(dsum)
        fd={}
        l=[]
        for i in dsum:
            fd[i]=deque()
            n=len(dsum[i])
            for j in range(n):
                left=(d[i][j]*(j+1))-dsum[i][j]
                right=(dsum[i][n-1]-dsum[i][j])-(d[i][j]*(n-j-1))
                #print(left,right)
                fd[i].append(left+right)
        #print(fd)
        for i in nums:
            l.append(fd[i].popleft())
        return l