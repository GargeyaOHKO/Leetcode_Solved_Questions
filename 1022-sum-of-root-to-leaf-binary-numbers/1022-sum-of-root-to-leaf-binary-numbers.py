# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res=[]
        def dfs(curr,l):
            if not curr.left and not curr.right:
                l.append(curr.val)
                self.res.append(l)
                return None
            if curr.left:
                dfs(curr.left,l+[curr.val])
            if curr.right:
                dfs(curr.right,l+[curr.val])
        dfs(root,[])
        s=0
        for i in self.res:
            power=len(i)-1
            for j in i:
                s+=j*(2**power)
                power-=1
        return s


             
