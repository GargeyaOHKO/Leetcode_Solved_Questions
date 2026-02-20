class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        dp={}
        def dfs(i):
            #print(i)
            if i>=len(s):
                return 1
            if i in dp:
                return dp[i]
            two,one=0,0
            if i<=len(s)-2:
                temp=s[i]+s[i+1]
                if int(temp)>=10 and int(temp)<=26:
                    two=dfs(i+2)
            if i<=len(s)-1:
                temp=s[i]
                if int(temp)>=1 and int(temp)<=9:
                    one=dfs(i+1)
            #print(one,two)
            dp[i]=one+two
            return dp[i]
        return dfs(0)
       