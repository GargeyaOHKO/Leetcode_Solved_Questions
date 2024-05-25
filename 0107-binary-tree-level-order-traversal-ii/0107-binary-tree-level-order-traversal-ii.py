# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        q=deque()
        q.append(root)
        fl=[]
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                fl.append(l)
        return fl[::-1]    
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        