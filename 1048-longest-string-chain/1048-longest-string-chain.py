class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        s=set(i for i in words)
        dp={}
        m=0
        def dfs(i,word,dp,curr):
            if (i,word,curr) in dp:
                return dp[(i,word,curr)]
            if i>=len(word):
                return curr
            newword=word[:i]+word[i+1:]
            if newword in s:
                dp[(i,word,curr)]=max([dfs(0,newword,dp,curr+1), dfs(i,newword,dp,curr+1), dfs(i+1,word,dp,curr)])
            else:
                dp[(i,word,curr)]=dfs(i+1,word,dp,curr)
            return dp[(i,word,curr)]
        
        for word in words:
            m=max(m,dfs(0,word,{},1))
            
        return m