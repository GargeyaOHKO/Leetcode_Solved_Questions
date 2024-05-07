# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        curr,stack=root,[]
        c=0
        while curr or stack:
            if curr:
                c+=1
                stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()
        return c        
        """
        :type root: TreeNode
        :rtype: int
        """
        