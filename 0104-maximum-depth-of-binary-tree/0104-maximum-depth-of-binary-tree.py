# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxdep=0
        curr,stack=root,[]
        c=0
        while curr or stack:
            if curr:
                c+=1
                stack.append([curr.right,c])
                curr=curr.left
                c+=1
                maxdep=max(maxdep,c)
            else:
                i=stack.pop()
                curr=i[0]
                c=i[1]
        return maxdep       
        """
        :type root: TreeNode
        :rtype: int
        """
        