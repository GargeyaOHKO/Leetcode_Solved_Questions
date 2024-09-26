class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d={'a':0,'e':1,'i':2,'o':3,'u':4}
        maxlen=0
        l=[0]*5
        newd={"00000":-1}
        for i in range(len(s)):
            if s[i] in d:
                l[int(d[s[i]])]+=1
                l[d[s[i]]]=l[d[s[i]]]%2
            ns=''.join(map(str,l))
            if ns not in newd:
                newd[ns]=i
            else:
                maxlen=max(maxlen,i-newd[ns])
        return maxlen