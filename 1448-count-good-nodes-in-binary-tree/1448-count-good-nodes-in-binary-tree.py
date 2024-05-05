# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(root,maxval):
            if not root:
                return 0
            if root.val>=maxval:
                res=1    
            else:
                res=0    
            maxval=max(maxval,root.val)
            res+=dfs(root.left,maxval)
            res+=dfs(root.right,maxval)    
            return res
        return dfs(root,root.val)       
        """
        :type root: TreeNode
        :rtype: int
        """
        