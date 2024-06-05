# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum=targetSum
        self.flag=False
        if not root:
            return False       
        self.dfs(root,0)
        return self.flag
    def dfs(self,root,currs):
        if not root:
            return 0
        else:
            #print(root.val,currs)
            currs+=root.val
            #print(root.val,currs)
            if not root.left and not root.right and currs==self.targetSum:
                self.flag=True    
            self.dfs(root.left,currs)
            self.dfs(root.right,currs)
        
        