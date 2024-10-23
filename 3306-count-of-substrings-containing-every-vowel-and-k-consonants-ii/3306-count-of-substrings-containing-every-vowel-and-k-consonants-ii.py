class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        d={'c':0,'a':0,'e':0,'i':0,'o':0,'u':0}
        vowel=('a','e','i','o','u')
        l=0
        c1=0
        for r in range(len(word)):
            if word[r] in vowel:
                d[word[r]]=d.get(word[r],0)+1
            else:
                d['c']+=1
            while d['a']>0 and d['e']>0 and d['i']>0 and d['o']>0 and d['u']>0 and d['c']>=k:
                c1+=len(word)-r
                if word[l] in vowel:
                    d[word[l]]=d.get(word[l],0)-1
                else:
                    d['c']-=1
                l+=1
            
        l=0
        c2=0
        d={'c':0,'a':0,'e':0,'i':0,'o':0,'u':0}
        for r in range(len(word)):
            if word[r] in vowel:
                d[word[r]]=d.get(word[r],0)+1
            else:
                d['c']+=1
            while d['a']>0 and d['e']>0 and d['i']>0 and d['o']>0 and d['u']>0 and d['c']>=(k+1):
                c2+=len(word)-r
                if word[l] in vowel:
                    d[word[l]]=d.get(word[l],0)-1
                else:
                    d['c']-=1
                l+=1
        return abs(c1-c2)