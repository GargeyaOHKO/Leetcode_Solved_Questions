class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        res=[]
        for i in queries:
            currnum=nums[i]
            if len(d[currnum])==1:
                res.append(-1)
            else:
                closest=float('inf')
                l,r=0,len(d[currnum])-1
                while l<=r:
                    mid=(l+r)//2
                    if d[currnum][mid]==i:
                        if mid==0:
                            closest=min(closest,len(nums)-abs(d[currnum][mid]-d[currnum][mid-1]))
                        else:
                            closest=min(closest,abs(d[currnum][mid]-d[currnum][mid-1]))
                        if mid==len(d[currnum])-1:
                            closest=min(closest,len(nums)-abs(d[currnum][(mid+1)%len(d[currnum])]-d[currnum][mid]))
                        else:
                            closest=min(closest,d[currnum][mid+1]-d[currnum][mid])
                        res.append(closest)
                        break
                    elif i<d[currnum][mid]:
                        r=mid-1
                    elif i>d[currnum][mid]:
                        l=mid+1       
        return res