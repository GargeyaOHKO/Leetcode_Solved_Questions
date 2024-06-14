# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        d={}
        def dfs(root,c,r):
            if not root:
                return None
            else:
                if c not in d:
                    d[c]=[(r,root.val)]
                else:
                    d[c].append((r,root.val))
                dfs(root.left,c-1,r+1)
                dfs(root.right,c+1,r+1)  
            return None   
        dfs(root,0,0)     
        #print(d)
        mini=min(d)
        maxi=max(d)
        tl,fl,l=[],[],[]       
        for i in range(mini,maxi+1):
            l.append(sorted(d[i]))
        #print(l)    
        for i in l:
            tl=[]
            for j in i:
                tl.append(j[1])
            fl.append(tl)    
        return fl                       
        