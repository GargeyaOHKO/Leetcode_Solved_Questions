class Solution:
    def compressedString(self, word: str) -> str:
        cur=word[0]
        c=1
        s=""
        for i in range(1,len(word)):
            if cur!=word[i] or c==9:
                s+=str(c)+cur
                cur=word[i]
                c=1
            else:
                c+=1
        s+=str(c)+cur
        return s

