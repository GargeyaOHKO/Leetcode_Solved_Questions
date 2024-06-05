# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l=0
        fl=[]
        def dfs(root,l):
            if not root:
                return None
            else:
                l=l*10+root.val
                if not root.right and not root.left:
                    fl.append(l)
                dfs(root.left,l)
                dfs(root.right,l)
        s=0       
        dfs(root,l)       
        for i in fl:
            s+=i
        return s
        