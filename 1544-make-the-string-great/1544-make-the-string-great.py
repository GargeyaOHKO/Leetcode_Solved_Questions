class Solution(object):
    def makeGood(self, s):
        i=0
        res=""
        stack=[]
        for i in range(len(s)):
            if ord(s[i])<=122 and ord(s[i])>=97:
                stack.append(s[i])
            else:
                if abs(ord(s[i])-ord(stack[-1]))==32:
                    stack.pop()       
        for i in stack:
            res+=i
        return res                
        """
        :type s: str
        :rtype: str
        """
        