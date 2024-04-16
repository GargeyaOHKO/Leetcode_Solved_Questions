# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res,c=[],1
        q=collections.deque()
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if c%2==0 and level:
                res.append(level[::-1])
            else:                              
                if level:
                    res.append(level)
            c+=1     
        return (res)
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        