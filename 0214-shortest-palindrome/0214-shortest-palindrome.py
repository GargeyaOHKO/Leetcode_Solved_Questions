class Solution:
    def shortestPalindrome(self, s: str) -> str:
        e=0
        #rs=s[::-1]
        mod=10**9+7
        n1,n2=0,0
        mul=1
        for i in range(len(s)):
            n1=((n1*29)+(ord(s[i])-96))%mod
            n2=(n2+((ord(s[i])-96)*mul))%mod
            mul*=29
            if n1==n2:
                e=i+1
        return s[e:][::-1]+s
