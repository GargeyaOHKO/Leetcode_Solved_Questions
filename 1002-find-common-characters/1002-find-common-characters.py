class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d={}
        for i in range(len(words[0])):
            d[words[0][i]]=d.get(words[0][i],0)+1
        #print(d) 
        for i in range(1,len(words)):
            tempd={}
            for j in range(len(words[i])):
                tempd[words[i][j]]=tempd.get(words[i][j],0)+1
            for i in d:
                if i not in tempd:
                    d[i]=0  
                else:
                    d[i]=min(d[i],tempd[i])    
        print(d)
        l=[]
        for i in d:
            for j in range(d[i]):
                l.append(i)
        return l    