# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        res=[]
        vis=[False]
        stack=[root]
        while stack:
            curr,v=stack.pop(),vis.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)    
                    vis.append(True)
                    stack.append(curr.right)
                    vis.append(False)
                    stack.append(curr.left)
                    vis.append(False)
        return res


        """
        :type root: TreeNode
        :rtype: List[int]
        """
        