class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        l=[]
        for i in queries:
            for j in dictionary:
                c=0
                for k in range(len(i)):
                    if i[k]!=j[k]:
                        c+=1
                if c<=2:
                    l.append(i)
                    break
        return l