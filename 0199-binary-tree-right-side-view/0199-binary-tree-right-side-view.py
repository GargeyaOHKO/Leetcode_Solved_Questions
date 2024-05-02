# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                res.append(l)        
        fl=[]
        for i in res:
            fl.append(i[-1])
        return fl    
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        