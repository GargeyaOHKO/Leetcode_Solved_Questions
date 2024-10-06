class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        l1=list(s1.strip().split(" "))
        l2=list(s2.strip().split(" "))
        if len(l1)>len(l2):
            l1[:],l2[:]=l2[:],l1[:]
        d1=Counter(l1)
        d2=Counter(l2)
        rem=[]
        if " ".join(l1)==" ".join(l2[:len(l1)]) or " ".join(l1)==" ".join(l2[len(l2)-len(l1):]):
            return True
            return False
        if len(l1)==len(l2):
            for i in range(len(l1)):
                if l1[i]!=l2[i]:
                    return False
            return True

        for i in l2:
            if i not in d1:
                rem.append(i)
            else:
                d1[i]-=1
                if d1[i]==0:
                    del d1[i]    
        if rem==len(l2):
            return False
        if " ".join(rem)+" "+" ".join(l1)==" ".join(l2) or " ".join(l1)+" "+" ".join(rem)==" ".join(l2):
            return True
        
        for i in range(len(l1)):
            if " ".join(l1[:i])+" "+" ".join(rem)+" "+" ".join(l1[i:])==" ".join(l2):
                return True
        return False
            
