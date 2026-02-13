class Solution:
    def longestWord(self, words: List[str]) -> str:
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        maxlen,res=0,[]
        words.sort(reverse=True)
        for i in words:
            n=len(i)
            flag=False
            temp=i
            for j in range(n-1):
                temp=temp[:-1]
                if temp not in d:
                    flag=True
                    break
            if not flag:
                if len(i)>maxlen:
                    maxlen=len(i)
                    res.append(i)
                elif len(i)==maxlen:
                    res.append(i)
        res.sort()
        return res[0]

