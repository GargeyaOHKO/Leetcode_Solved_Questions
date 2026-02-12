class Solution:
    def longestBalanced(self, s: str) -> int:
        mlen=0
        for i in range(len(s)):
            d,maxf,uniq={},float("-inf"),0
            for j in range(i,len(s)):
                if s[j] not in d:
                    uniq+=1
                d[s[j]]=d.get(s[j],0)+1
                maxf=max(maxf,d[s[j]])
                if maxf*uniq==(j-i+1):
                    mlen=max(mlen,j-i+1)
        return mlen