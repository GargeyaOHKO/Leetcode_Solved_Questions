class Solution(object):
    def maxDepth(self, s):
        c=0
        maxc=0
        for i in s:
            if i=='(':
                c+=1
            elif i==')':
                c-=1
            maxc=max(c,maxc)     
        return maxc       
        """
        :type s: str
        :rtype: int
        """
        