# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        def dfs(root,l):
            if not root:
                return None
            else:
                if not root.left and not root.right:
                    l.append(root.val)
                dfs(root.left,l)
                dfs(root.right,l)
                return l
        dfs(root1,l1)
        dfs(root2,l2) 
        if l1==l2:
            return True
        else:
            return False    

        