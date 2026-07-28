class Solution:
    def smallestPalindrome(self, s: str) -> str:
        front,mid=[],[]
        d=Counter(s)
        for i in range(97,97+27):
            if chr(i) in d:
                if d[chr(i)]%2==0:
                    front.append(chr(i)*(d[chr(i)]//2))
                else:
                    front.append(chr(i)*(d[chr(i)]//2))
                    mid.append(chr(i))
        res=""
        for i in front:
            res+=i
        for i in mid:
            res+=i
        for i in front[::-1]:
            res+=i
        return res


