class Solution(object):
    def checkInclusion(self, s1, s2):    
        if len(s2)<len(s1):
            return False
        d1={}
        d2={}
        for i in range(len(s1)):
            d1[s1[i]]=d1.get(s1[i],0)+1
            d2[s2[i]]=d2.get(s2[i],0)+1                 
        if d1==d2: return True       
        l=0 
        for r in range(len(s1),len(s2)):
            d2[s2[r]]=d2.get(s2[r],0)+1
            d2[s2[l]]-=1
            if d2[s2[l]]==0: del d2[s2[l]]
            if d1==d2: return True    
            l+=1
        return False            
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        