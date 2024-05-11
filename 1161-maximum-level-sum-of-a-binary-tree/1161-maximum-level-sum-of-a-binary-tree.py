# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res=[]
        q=deque()
        q.append(root)
        c=1
        while q:
            s=0
            flag=False
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    s+=node.val
                    flag=True
                    q.append(node.left)
                    q.append(node.right)
            if flag:
                res.append([s,c])
                c+=1
        print(res)    
        return max(res)[1]    
        
        