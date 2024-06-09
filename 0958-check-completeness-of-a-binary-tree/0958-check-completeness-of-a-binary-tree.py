# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q=deque()
        q.append(root)
        flag=True
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    if flag==False:
                        return False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    flag=False    
        return True            