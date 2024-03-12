class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        l,r=0,len(tokens)-1
        maxc,c=0,0
        while l<=r:
            if tokens[l]<=power:
                power-=tokens[l]
                c+=1
                l+=1
            elif c>0:
                power+=tokens[r]
                c-=1
                r-=1
            if c<1 and tokens[l]>power:
                break    
            maxc=max(maxc,c)
        return maxc
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        