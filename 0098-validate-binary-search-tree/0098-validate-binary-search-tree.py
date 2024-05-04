# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        curr,stack=root,[]
        res=[]
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                res.append(curr.val)    
                curr=curr.right  
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True
        """
        :type root: TreeNode
        :rtype: bool
        """
        