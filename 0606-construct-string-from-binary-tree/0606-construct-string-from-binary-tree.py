# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        s=[]
        def dfs(root):
            if not root:
                return None
            else:
                s.append("(")
                s.append(str(root.val))
                if root.right and not root.left:
                    s.append("()")
                dfs(root.left)
                dfs(root.right)
                s.append(")")
        dfs(root)            
        return "".join(s)[1:-1]            
        """
        :type root: TreeNode
        :rtype: str
        """
        