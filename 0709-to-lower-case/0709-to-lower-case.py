class Solution(object):
    def toLowerCase(self, s):
        ans=""
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                add=ord(i)-65
                ans+=chr(97+add)
            else:
                ans+=i   
        return ans            
        """
        :type s: str
        :rtype: str
        """
        