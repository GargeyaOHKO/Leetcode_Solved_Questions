class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        avail=set(wordDict)
        dp={}
        def dfs(i,w):
            #print(w)
            if (i,w) in dp:
                return dp[(i,w)]
            if i>=len(s):
                if w=="":
                    return True
                else:
                    return False
            w+=s[i]
            if w in avail:
                dp[(i,w)]=dfs(i+1,"") or dfs(i+1,w)
            else:
                dp[(i,w)]=dfs(i+1,w)
            return dp[(i,w)]
        return dfs(0,"")