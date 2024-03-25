class Solution(object):
    def maxScore(self, cardPoints, k):
        s=0
        for i in range(k):
            s+=cardPoints[i]       
        maxs=s    
        l=k-1
        r=len(cardPoints)-1
        while l>=0:
            s-=cardPoints[l]
            s+=cardPoints[r]
            l-=1
            r-=1
            maxs=max(maxs,s)
        return maxs         
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        