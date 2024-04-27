class Solution(object):
    def checkValidString(self, s):
        if s[0]==')' or s[-1]=='(':
            return False
        lmin,lmax=0,0
        for i in s:
            if i == '(':
                lmin,lmax=lmin+1,lmax+1
            elif i ==')':
                lmin,lmax=lmin-1,lmax-1
            else:
                lmin,lmax=lmin-1,lmax+1
            if lmin<0:
                lmin=0
        return lmin==0                                   
        """
        :type s: str
        :rtype: bool
        """
        