class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            d[i]=d.get(i,0)+1
        d={k:v for k,v in sorted(d.items(), key=lambda item:item[1],reverse=True)}
        #print(d)
        c=0
        res=0
        for i in d:
            #print(c,i)
            if c<8:
                res+=1*d[i]
            elif c>=8 and c<16:
                res+=2*d[i]
            else:
                res+=3*d[i]
            c+=1
        return res