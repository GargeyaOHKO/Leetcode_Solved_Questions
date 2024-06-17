# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        parent={}
        q=deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                    parent[node.right]=node
                if node.left:
                    q.append(node.left)
                    parent[node.left]=node
        q=deque([(target,0)])
        vis=set([target])
        res=[]
        while q:
            for i in range(len(q)):
                node,c=q.popleft()
                if c==k:
                    res.append(node.val)
                else:
                    if node.left and node.left not in vis:
                        q.append([node.left,c+1])
                        vis.add(node.left)
                    if node.right and node.right not in vis:
                        q.append([node.right,c+1])
                        vis.add(node.right)
                    if node in parent and parent[node] not in vis:
                        q.append([parent[node],c+1])
                        vis.add(parent[node])
        #print(q)
        return res

        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        