class Solution(object):
    def minimumLength(self, s):
        l=0
        r=len(s)-1
        w=""
        while l<r:
            if s[l]==s[r]:
                w=s[l]
            else:
                flag=False
                break
            while l<len(s) and s[l]==w:
                l+=1
            while r>0 and s[r]==w:
                r-=1
        return len(s[l:r+1])        
        """
        :type s: str
        :rtype: int
        """
        