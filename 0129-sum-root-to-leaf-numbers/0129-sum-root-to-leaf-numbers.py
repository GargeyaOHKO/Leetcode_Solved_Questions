# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,l,fl):
            if not root:
                return None
            else:
                l.append(root.val)
                if not root.right and not root.left:
                    fl.append(list(l))
                else:    
                    dfs(root.left,l,fl)
                    dfs(root.right,l,fl)
                l.pop()     
        l=[]
        fl=[]          
        dfs(root,l,fl)       
        ans=0
        for i in fl:
            s=""
            for j in range(len(i)): 
                s+=str(i[j])
            ans+=int(s)   
        return ans     
