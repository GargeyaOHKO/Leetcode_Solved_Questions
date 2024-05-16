# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        if root.val==0 or root.val==1:
            return root.val
        if root.val==2:
            return self.evaluateTree(root.right) or self.evaluateTree(root.left)
        if root.val==3:
            return self.evaluateTree(root.right) and self.evaluateTree(root.left)        
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        