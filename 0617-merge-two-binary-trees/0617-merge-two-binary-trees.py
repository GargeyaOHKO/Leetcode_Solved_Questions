# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2
        elif not root2 and root1:
            return root1
        elif not root1 and not root2:
            return None
        def merge(root1,root2):
            if not root1 and not root2:
                return None
            root=TreeNode(0)
            if root1:
                root.val+=root1.val
            else:
                root1=TreeNode(0)
            if root2:
                root.val+=root2.val
            else:
                root2=TreeNode(0)
            root.left=merge(root1.left,root2.left)
            root.right=merge(root1.right,root2.right)      
            
            return root
        return merge(root1, root2)    
        