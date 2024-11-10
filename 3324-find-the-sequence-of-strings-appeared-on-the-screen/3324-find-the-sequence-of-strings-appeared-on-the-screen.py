class Solution:
    def stringSequence(self, target: str) -> List[str]:
        l=[]
        s=""
        for i in range(len(target)):
            c=97
            while chr(c)!=target[i]:
                #print(chr(c))
                l.append(s+chr(c))
                c+=1
            s+=target[i]
            l.append(s)
        return l
        