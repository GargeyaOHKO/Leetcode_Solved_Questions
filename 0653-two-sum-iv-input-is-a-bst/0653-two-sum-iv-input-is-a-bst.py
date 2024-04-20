# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        curr,stack=root,[]
        d={}
        while curr or stack:
            if curr:
                #print(d,curr.val)
                if (k-curr.val) in d:
                    return True
                d[curr.val]=0
                stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()            
        return False        
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        