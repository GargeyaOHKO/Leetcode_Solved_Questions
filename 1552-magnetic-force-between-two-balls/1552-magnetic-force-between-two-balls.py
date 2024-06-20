class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        print(position)
        if m==2:
            return abs(position[0]-position[-1])
        ans=0
        l,r=0,max(position)
        while l<=r:
            mid=(l+r)//2
            print(mid)
            curr=0
            count=1
            for i in range(curr,len(position)):
                if (position[i]-position[curr])>=mid:
                    count+=1
                    curr=i
            if count>=m:
                ans=max(mid,ans)
                l=mid+1
            elif count<m:
                r=mid-1
        return ans

        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        