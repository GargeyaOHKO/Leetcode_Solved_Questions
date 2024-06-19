class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay)<(m*k):
            return -1
        else:
            l=min(bloomDay)
            r=max(bloomDay)
            boq=0
            while l<=r:
                mid=(l+r)//2
                c=0
                nob=0
                for i in range(len(bloomDay)):
                    if bloomDay[i]<=mid:
                        c+=1
                    else:
                        c=0
                    if c==k:
                        c=0
                        nob+=1        
                if nob<m:
                    l=mid+1
                elif nob>=m:
                    boq=mid
                    r=mid-1
            return boq                   
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        