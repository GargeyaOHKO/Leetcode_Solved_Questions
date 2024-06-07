class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d={}
        for i in dictionary:
            d[i]=0
        l=list(map(str,sentence.split(" ")))
        #print(d,l)        
        for i in range(len(l)):
            s=""
            for j in range(len(l[i])):
                s+=l[i][j]
                if s in d:
                    l[i]=s
                    break
        s=""
        for i in range(len(l)):
            if i==len(l)-1:
                s+=l[i]
            else:
                s+=l[i]+" "
        return s        
