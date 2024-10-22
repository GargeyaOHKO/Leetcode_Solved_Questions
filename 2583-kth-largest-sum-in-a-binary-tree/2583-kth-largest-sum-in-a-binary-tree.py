# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=collections.deque()
        q.append(root)
        h=[]
        while q:
            s=0
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    s+=node.val
                    q.append(node.left)
                    q.append(node.right)
            if s>0:
                heapq.heappush(h,-s)
        if k>len(h):
            return -1
        for i in range(k):
            r=heapq.heappop(h)
        return abs(r)
                    