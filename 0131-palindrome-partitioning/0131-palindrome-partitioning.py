class Solution(object):
    def partition(self, s):
        res=[]

        def dfs(i,l):
            #print(i,len(s))
            if i>=len(s):
                res.append(list(l))
                return None

            for end in range(i,len(s)):
                if s[i:end+1]==s[i:end+1][::-1]:
                    l.append(s[i:end+1])
                    dfs(end+1,l)
                    l.pop()
            #return res
        dfs(0,[])
        return res
        """
        :type s: str
        :rtype: List[List[str]]
        """
        