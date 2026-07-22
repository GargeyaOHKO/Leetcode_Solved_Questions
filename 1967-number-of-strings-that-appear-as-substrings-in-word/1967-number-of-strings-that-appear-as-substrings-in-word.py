class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        s=set()
        for i in range(len(word)):
            c=""
            for j in range(i,len(word)):
                c+=word[j]
                s.add(c)
        c=0
        for i in patterns:
            if i in s:
                c+=1
        return c
