class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        l1=list(s1.strip().split(" "))
        l2=list(s2.strip().split(" "))
        if len(l1)>len(l2):
            l2[:],l1[:]=l1[:],l2[:]
        d1=Counter(l1)
        d2=Counter(l2)
        if len(l1)==len(l2):
            for i in range(len(l2)):
                if l1[i]!=l2[i]:
                    return False
            return True
        c=0
        for i in l2:
            if i in d1:
                c+=1
        if c==0:
            return False
        for i in l1:
            if i not in d2:
                return False
        c=0
        f1=False
        f11=True
        for i in l2:
            #print(i)
            #print(c,f1)
            if i not in d1 and c==0:
                c+=1
            elif c==1 and i in d1 and f1==False:
                f1=True
            elif f1==True and i not in d1:
                f11=False
                break
            if i in d1:
                d1[i]-=1
                if d1[i]==0:
                    del d1[i]
        l2.reverse()
        print(l2)
        c=0
        d1=Counter(l1)
        f2=False
        f22=True
        for i in l2:
            if i not in d1 and c==0:
                c+=1
            elif c==1 and i in d1 and f2==False:
                f2=True
            elif f2==True and i not in d1:
                f22=False
            if i in d1:
                d1[i]-=1
                if d1[i]==0:
                    del d1[i]
        if f11 or f22:
            return True
        else:
            return False
            

        