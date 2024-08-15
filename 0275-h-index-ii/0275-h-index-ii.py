class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        l,r=0,n-1
        if citations[-1]==0:
            return 0
        res=0
        while l<=r:
            mid=l+((r-l)//2)
            if citations[mid]>=(n-mid):
                res=n-mid
                r=mid-1
            else:
                l=mid+1
        return res

        