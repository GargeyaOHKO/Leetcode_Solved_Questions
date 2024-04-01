class Solution(object):
    def lengthOfLastWord(self, s):
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and c==0:
                continue
            if s[i]!=" ":
                c+=1
            elif s[i]==" ":
                return c    
        return c        

        """
        :type s: str
        :rtype: int
        """
        