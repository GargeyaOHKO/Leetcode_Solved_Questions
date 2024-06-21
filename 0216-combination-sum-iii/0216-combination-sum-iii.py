class Solution(object):
    def combinationSum3(self, k, n):
        l=[1,2,3,4,5,6,7,8,9]
        res=[]
        templ=[]
        def dfs(i,sumation,count,templ):
            #print(count , sumation , templ)
            if sumation==n and count==k:
                res.append(list(templ))
                return None
            if i>=len(l) or sumation>n or count>k:
                return None
            
            templ.append(l[i])
            dfs(i+1,sumation+l[i],count+1,templ)
            #print(templ)
            templ.pop()
            dfs(i+1,sumation,count,templ)
            return res
        #print(res)
        return dfs(0,0,0,[])



        
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        