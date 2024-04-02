class Solution(object):
    def isIsomorphic(self, s, t):
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=t[i]
            else:
                if d1[s[i]]!=t[i]:
                    return False    
            
            if t[i] not in d2:
                d2[t[i]]=s[i]
            else:
                if d2[t[i]]!=s[i]:
                    return False

        return True            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       