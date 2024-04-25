# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        curr,stack=p,[]
        res1,res2=[],[]
        while curr or stack:
            if curr:
                res1.append(curr.val)
                stack.append(curr.right)
                curr=curr.left
            else:
                res1.append('a')
                curr=stack.pop()
        curr,stack=q,[]
        while curr or stack:
            if curr:
                res2.append(curr.val)
                stack.append(curr.right)
                curr=curr.left
            else:
                res2.append('a')
                curr=stack.pop()
        if res1==res2:
            return True
        else:
            return False        
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        