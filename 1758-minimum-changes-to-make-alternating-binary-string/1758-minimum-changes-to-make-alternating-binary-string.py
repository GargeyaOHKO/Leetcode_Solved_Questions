class Solution:
    def minOperations(self, s: str) -> int:
        c1,c2=0,0
        for i in range(len(s)):
            if i%2==0:
                if int(s[i])==0:
                    c1+=1
                if int(s[i])==1:
                    c2+=1
            else:
                if int(s[i])==1:
                    c1+=1
                if int(s[i])==0:
                    c2+=1
        return min(c1,c2)