# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent={}
        curr=root
        stack=[]
        curr1=None
        while curr or stack:
            if curr:
                if curr.val==startValue:
                    curr1=curr
                if curr.left:
                    parent[curr.left]=curr
                if curr.right:
                    parent[curr.right]=curr
                stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()

        q=deque([(curr1,"")])
        vis=set([curr1])
        res=[]
        while q:
            for i in range(len(q)):
                node,s=q.popleft()
                if node.val==destValue:
                    return s
                    break
            else:
                if node.left and node.left not in vis:
                    q.append([node.left,s+'L'])
                    vis.add(node.left)
                if node.right and node.right not in vis:
                    q.append([node.right,s+'R'])
                    vis.add(node.right)
                if node in parent and parent[node] not in vis:
                    q.append([parent[node],s+'U'])
                    vis.add(parent[node])

        