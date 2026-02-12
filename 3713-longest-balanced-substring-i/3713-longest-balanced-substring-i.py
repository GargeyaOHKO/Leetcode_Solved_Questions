class Solution:
    def longestBalanced(self, s: str) -> int:
        mlen=0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                d[s[j]]=d.get(s[j],0)+1
                var,flag=0,False
                for z in d:
                    if var==0:
                        var=d[z]
                    else:
                        if var!=d[z]:
                            flag=True
                if not flag:
                    mlen=max(mlen,j-i+1)
        return mlen