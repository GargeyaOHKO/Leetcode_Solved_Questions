# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root.right==None and root.left==None:
            return 0
        c=0
        curr,stack=root,[]
        right=[]
        while curr or stack:
            if curr:
                stack.append(curr.right)
                if curr.right:
                    right.append(curr.right)
                if curr.left==None and curr.right==None and curr not in right:
                    #print(curr.val)
                    c+=curr.val
                curr=curr.left
            else:
                #print(stack)
                curr=stack.pop()        
        return c        
        """
        :type root: TreeNode
        :rtype: int
        """
        