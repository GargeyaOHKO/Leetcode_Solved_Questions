# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l=0
        self.s=0
        fl=[]
        def dfs(root,l):
            if not root:
                return None
            else:
                l=l*10+root.val
                if not root.right and not root.left:
                    self.s+=l
                dfs(root.left,l)
                dfs(root.right,l)
                return self.s               
        return dfs(root,l)       
        