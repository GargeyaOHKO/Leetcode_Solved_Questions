class Solution(object):
    def validStrings(self, n):
        res=[]
        def dfs(i,count,s):
            if len(s)>1 and s[-1]=='0' and s[-1]==s[-2]:
                return None
            if i==n:
                    res.append(str(s))
                    return None
            s+='1'            
            dfs(i+1,count+1,s)
            s=s[:-1]
            s+='0'
            dfs(i+1,count,s)
            return res
        return dfs(0,0,"") 
        """
        :type n: int
        :rtype: List[str]
        """
        