class Solution(object):
    def maximumOddBinaryNumber(self, s):
        l=len(s)
        count=0
        ns=''
        for i in range(l):
            if s[i]=='1':
                count=count+1
        for i in range(l-1):
            if count>1:
                ns=ns+'1'
                count=count-1
            else:
                ns=ns+'0'
        ns=ns+'1'       
        return ns    
        """
        :type s: str
        :rtype: str
        """
        