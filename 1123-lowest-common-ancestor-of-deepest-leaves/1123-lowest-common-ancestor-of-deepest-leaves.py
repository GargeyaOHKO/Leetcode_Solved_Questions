# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        l,fl=[],[]
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    l.append(node)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                fl=l 

        if len(fl)==1:
            return fl[0] 

        a,b=fl[0],fl[-1]

        def dfs(root,a,b):
            if not root:
                return None
            if root.val==a.val or root.val==b.val:
                return root
            left=dfs(root.left,a,b)
            right=dfs(root.right,a,b)
            if left and not right:
                return left
            if right and not left:
                return right
            if right and left:
                return root
            return None    
        return dfs(root,a,b)                


