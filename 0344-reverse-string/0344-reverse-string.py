class Solution(object):
    def reverseString(self, s):
        """for i in range(0,len(s)//2):
            s[i],s[-1-i]=s[-1-i],s[i]"""
        i=0
        l=len(s)-1
        while(i<l):
            s[i],s[l]=s[l],s[i]  
            i+=1
            l-=1   

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        