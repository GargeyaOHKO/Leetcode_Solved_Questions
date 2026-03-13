class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d={}
        for i in range(len(isConnected)):
            l=[]
            for j in range(len(isConnected[0])):
                if j!=i and isConnected[i][j]==1:
                    l.append(j+1)
            d[i+1]=l
        self.c=0
        def dfs(node,flag):
            if not flag:
                self.c+=1
            for nnode in d[node]:
                if nnode not in seen:
                    seen.add(nnode)
                    dfs(nnode,True)
        seen=set()
        for i in d:
            if i not in seen:
                dfs(i,False)
            seen.add(i)
        return self.c