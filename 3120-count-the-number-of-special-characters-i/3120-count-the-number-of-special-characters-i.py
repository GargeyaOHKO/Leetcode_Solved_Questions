class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small=set()
        capital=set()
        c=0
        for i in word:
            if 97<=ord(i)<=122:
                small.add(ord(i)-97)
            if 65<=ord(i)<=90:
                capital.add(ord(i)-65)
        for i in small:
            if i in capital:
                c+=1
        return c 