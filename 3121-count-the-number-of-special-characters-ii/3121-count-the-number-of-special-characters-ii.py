class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d={}
        seen=set()
        c=0
        for i in range(len(word)-1,-1,-1):
            if 97<=ord(word[i])<=122 and ord(word[i])-97 not in d:
                d[ord(word[i])-97]=i
        for i in range(len(word)):
            if 65<=ord(word[i])<=90 and ord(word[i]) not in seen:
                if ord(word[i])-65 in d:
                    if i>d[ord(word[i])-65]:
                        c+=1
                seen.add(ord(word[i]))
        return c
