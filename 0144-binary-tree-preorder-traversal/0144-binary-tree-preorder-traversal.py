# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        curr,stack=root,[]
        res=[]
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr=curr.left
            else:    
                curr=stack.pop()                
        return res
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        