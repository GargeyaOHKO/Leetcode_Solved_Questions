# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        def dfs(root,c):
            if not root:
                return None
            else:
                l.append([root.val,c])
                dfs(root.left,c-1)
                dfs(root.right,c+1)  
            return None   
        dfs(root,0)
        d={}
        maxi,mini=float("-inf"),float("inf")
        for i in l:
            if i[1] not in d:
                maxi=max(maxi,i[1])
                mini=min(mini,i[1])
                d[i[1]]=[i[0]]
            else:
                d[i[1]].append(i[0])     
        #print(d)

        q,d2=deque(),{}
        q.append(root)
        c=-1
        while q:
            tl=[]
            c+=1
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    if node.val not in d2:
                        d2[node.val]=[c]
                    else:
                        d2[node.val].append(c)
                    q.append(node.left)
                    q.append(node.right)  
        #print(d2)
        l=[]        
        for i in range(mini,maxi+1):
            j=0
            while j<len(d[i])-1:
            #for j in range(len(d[i])-1):
                if (d2[d[i][j]]==d2[d[i][j+1]] and d[i][j]>d[i][j+1]) or d2[d[i][j]]>d2[d[i][j+1]]:
                    d[i][j],d[i][j+1]=d[i][j+1],d[i][j]
                    j=0
                else:
                    j+=1
            l.append(d[i])        
        #print(l) 
        return l                       
        