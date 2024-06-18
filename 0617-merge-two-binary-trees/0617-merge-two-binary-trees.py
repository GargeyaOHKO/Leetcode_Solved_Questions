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
        head=TreeNode(0)
        def merge(head,root1,root2):
            if not root1 and not root2:
                return None
            if not root1 and root2:
                root1=TreeNode(0)
            if not root2 and root1:
                root2=TreeNode(0)
            head=TreeNode(root1.val+root2.val)
            head.left=merge(head.left,root1.left,root2.left)
            head.right=merge(head.right,root1.right,root2.right)      
            return head
        return merge(head,root1,root2)    
        