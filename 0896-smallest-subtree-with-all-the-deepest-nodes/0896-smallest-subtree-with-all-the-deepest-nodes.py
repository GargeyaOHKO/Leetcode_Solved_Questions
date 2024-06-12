# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
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
        #print(fl)
        if len(fl)==1:
            return fl[0]
        a,b=fl[0],fl[-1]    
        def dfs(root,a,b):
            if not root:
                return None
            if root==a or root==b:
                return root
            left=dfs(root.left,a,b)
            right=dfs(root.right,a,b)
            if not left:
                return right
            if not right:
                return left
            return root
        return dfs(root,a,b)
        