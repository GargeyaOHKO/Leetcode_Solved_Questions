class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        l=[]
        s=0
        for i in word:
            s=(s*10+int(i))%m
            #print(s)
            if s%m==0:
                l.append(1)
            else:
                l.append(0)
        return l
        