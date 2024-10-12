class Solution:
    def shortestPalindrome(self, s: str) -> str:
        e=0
        mod=10**9+7
        n1,n2=0,0
        mul=1
        for i in range(len(s)):
            char=(ord(s[i])-96)
            n1=((n1*26))%mod
            n1=(n1+char)%mod
            add=(char*mul)%mod
            n2=(n2+add)%mod
            mul*=26
            if n1==n2:
                e=i+1
        pref=s[e:]
        return pref[::-1]+s
