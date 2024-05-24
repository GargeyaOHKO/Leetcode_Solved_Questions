class Solution(object):
    def reverseVowels(self, s):
        d={'a','e','i','o','u','A','E','I','O','U'}
        l=[]
        for i in range(len(s)):
            if s[i] in d:
                l.append(s[i])
                s=s[:i]+"_"+s[i+1:]      
        #print(l)        
        for i in range(len(s)):
            if s[i]=="_":
                if l: 
                    c=l.pop()
                    s=s[:i]+c+s[i+1:]
        return s        


        """
        :type s: str
        :rtype: str
        """
        