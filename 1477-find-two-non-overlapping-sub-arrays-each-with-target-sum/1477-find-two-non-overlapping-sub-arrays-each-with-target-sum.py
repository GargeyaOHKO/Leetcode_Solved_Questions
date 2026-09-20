class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        d=[float('inf')]*len(arr)
        total=0
        l=0
        res=float('inf')
        for r in range(len(arr)):
            total+=arr[r]
            while total>target:
                total-=arr[l]
                l+=1
            if r>0:
                d[r]=d[r-1]
            if total==target:
                length=r-l+1
                if l>0 and d[l-1]!=float('inf'):
                    res=min(res,length+d[l-1])
                d[r]=min(d[r],length)
                
        if res==float('inf'):
            return -1
        else:
            return res