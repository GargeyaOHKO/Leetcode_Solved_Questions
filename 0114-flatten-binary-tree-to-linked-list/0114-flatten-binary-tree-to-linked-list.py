# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        self.prev=None
        self.dfs(root)

    def dfs(self,root):
        if not root:
            return None
        else:
            self.dfs(root.right)
            self.dfs(root.left)    
            root.right=self.prev
            root.left=None
            self.prev=root    
        return root  

        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """ 