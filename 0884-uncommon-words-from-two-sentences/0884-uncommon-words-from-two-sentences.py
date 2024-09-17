class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1=list(s1.split(" "))
        l2=list(s2.split(" "))
        d1,d2={},{}
        for i in l1:
            d1[i]=d1.get(i,0)+1
        for i in l2:
            d2[i]=d2.get(i,0)+1
        l=[]
        for i in d1:
            if d1[i]==1 and i not in d2:
                l.append(i)
        for i in d2:
            if d2[i]==1 and i not in d1:
                l.append(i)
        return l
