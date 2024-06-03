class Solution(object):
    def appendCharacters(self, s, t):
        p1=0
        p2=0
        if len(s)=="":
            return len(t)
        if len(t)=="":
            return 0
        c=0
        while p1<len(s) and p2<len(t):
            if s[p1]==t[p2]:
                c+=1
                p1+=1
                p2+=1
            else:
                p1+=1
        return len(t)-c            

        """
        :type s: str
        :type t: str
        :rtype: int
        """
        