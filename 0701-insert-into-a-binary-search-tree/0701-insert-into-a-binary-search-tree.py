# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root==None:
            return TreeNode(val)
        curr=root 
        while curr:
            if curr.right==None or curr.left==None:
                if curr.left==None and curr.val>val:
                    curr.left=TreeNode(val)
                    break
                elif curr.right==None and curr.val<val:
                    curr.right=TreeNode(val)
                    break    
            if curr.val>val:
                curr=curr.left
            else:
                curr=curr.right    
        return root
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        