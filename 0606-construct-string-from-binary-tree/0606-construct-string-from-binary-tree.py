# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        self.s=""
        def dfs(root):
            if not root:
                return None
            else:
                self.s+=str(root.val)
                if not root.right and not root.left:
                    return 0
                if root.left:
                    self.s+="("
                    dfs(root.left)
                    self.s+=")"
                else:
                    self.s+="()"
                if root.right:
                    self.s+="("
                    dfs(root.right)
                    self.s+=")"                
        dfs(root)
        #print(self.s)
        return self.s
        """
        :type root: TreeNode
        :rtype: str
        """
        