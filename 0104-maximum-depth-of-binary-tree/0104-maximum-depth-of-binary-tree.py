# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            lh=self.maxDepth(root.left)
            rh=self.maxDepth(root.right)
            return max(lh,rh)+1
                       
        """
        :type root: TreeNode
        :rtype: int
        """
        