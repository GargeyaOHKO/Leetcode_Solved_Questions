class Solution(object):
    def isSubsequence(self, s, t):
        if s=='':
            return True
        p1=0
        c=0
        for i in range(len(t)):
            if s[p1]==t[i]:
                p1+=1
                c+=1
            if c==len(s):
                return True
        return False            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        