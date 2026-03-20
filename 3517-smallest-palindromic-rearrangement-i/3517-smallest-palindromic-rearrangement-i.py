class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        d=SortedDict()
        for i in s:
            d[i]=d.get(i,0)+1
        #print(d)
        s=""
        left=""
        for i in d:
            #print(d)
            while d[i]>0:
                if d[i]==1:
                    left=i
                    break
                else:
                    s+=i
                    d[i]-=2
        s=s+left+s[::-1]
        return s

