class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        d1=Counter(s1)
        d2={}
        i,j=0,len(s1)-1
        for z in range(i,j+1):
            d2[s2[z]]=d2.get(s2[z],0)+1
        while j<len(s2)-1:
            #print(d1,d2)
            if d1==d2:
                return True
            else:
                d2[s2[i]]-=1
                if d2[s2[i]]==0:
                    del d2[s2[i]]
                i+=1
                j+=1
                d2[s2[j]]=d2.get(s2[j],0)+1
        return False
        
