# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        else:
            rt=root.right
            root.right=root.left
            root.left=rt
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root               

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        