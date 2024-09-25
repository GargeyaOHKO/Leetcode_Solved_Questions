class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        l=[]
        for i in words:
            s=""
            c=0
            for j in i:
                s+=j
                for z in words:
                    #print(s,z[:len(s)])
                    if s==z[:len(s)]:
                        c+=1 
            l.append(c)
        return l
        