class Solution(object):
    def longestPalindrome(self, s):
        d={}
        l=0
        ho=0
        flag=False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1        
        for i in d:
            if d[i]%2==0:
                l=l+d[i]
            else:
                l=l+d[i]-1
                flag=True           
        if flag:
            return ho+l+1 
        else:
            return l               
        """
        :type s: str
        :rtype: int
        """
        