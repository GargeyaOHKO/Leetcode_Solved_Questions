class Solution(object):
    def minWindow(self, s, t):
        if len(t)>len(s):
            return ""
        d1,d2={},{} 
        for i in t:
            d1[i]=d1.get(i,0)+1

        curr,req=0,len(d1)
        ss,maxl=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            d2[s[r]]=d2.get(s[r],0)+1
            if s[r] in d1 and d1[s[r]]==d2[s[r]]:
                curr+=1
            while curr==req:
                if (r-l+1)<maxl:
                    maxl=r-l+1
                    ss=[l,r]
                d2[s[l]]-=1                        
                if s[l] in d1 and d2[s[l]]<d1[s[l]]:
                    curr-=1   
                l+=1            
        return s[ss[0]:ss[1]+1]    
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        