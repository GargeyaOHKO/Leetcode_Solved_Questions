class Solution(object):
    def checkInclusion(self, s1, s2):    
        if len(s2)<len(s1):
            return False
        d1={}
        d2={}
        for i in s1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in range(len(s1)):
            if s2[i] not in d2:
                d2[s2[i]]=1
            else:
                d2[s2[i]]+=1  
        if d1==d2:
            return True        

        l=0
        r=len(s1)   
        while r<len(s2):
            print(d1,d2)
            if d1==d2:
                return True
            else:
                if s2[r] not in d2:
                    d2[s2[r]]=1
                else:    
                    d2[s2[r]]+=1
                d2[s2[l]]-=1
                if d2[s2[l]]==0:
                    del d2[s2[l]]
                if d1==d2:
                    return True    
                r+=1
                l+=1
        return False            

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        