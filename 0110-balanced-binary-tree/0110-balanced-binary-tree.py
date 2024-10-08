# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True,0]
            else:
                left,right=dfs(root.left),dfs(root.right)
                if left[0]==True and right[0]==True and abs(left[1]-right[1])<=1:
                    balanced=True
                else:
                    return False
            return [balanced,(1+max(left[1],right[1]))]
        return dfs(root)                    
        """
        :type root: TreeNode
        :rtype: bool
        """
        