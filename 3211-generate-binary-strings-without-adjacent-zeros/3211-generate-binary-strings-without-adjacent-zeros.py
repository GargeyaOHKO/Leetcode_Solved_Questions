class Solution(object):
    def validStrings(self, n):
        res=[]
        dp={}
        def dfs(i,count,s):
            if len(s)>1 and s[-1]=='0' and s[-1]==s[-2]:
                return None
            if i==n:
                    res.append(str(s))
                    return None
            if (i,s) in dp:
                return dp[(i,s)]
            s+='1'            
            dfs(i+1,s)
            s=s[:-1]
            s+='0'
            dfs(i+1,s)
            return res
        return dfs(0,0,"") 
        """
        :type n: int
        :rtype: List[str]
        """
        