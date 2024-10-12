class Solution:
    def shortestPalindrome(self, s: str) -> str:
        e=0
        rs=s[::-1]
        n1,n2=0,0
        for i in range(len(s)):
            n1=(n1*29)+(ord(s[i])-96)
            n2=n2+((ord(rs[-1-i])-96)*(29**i))
            #print(n1)
            #print(n2)
            if n1==n2:
                e=i+1
        return s[e:][::-1]+s
