# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        d={}
        def dfs(root):
            if not root:
                return None
            if root.left:
                d[root.left]=root
            if root.right:
                d[root.right]=root
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        leaf=[]
        curr,stack=root,[]
        while curr or stack:
            if curr:
                if not curr.left and not curr.right:
                    leaf.append(curr)
                stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()
        count=0
        for i in leaf:
            q=deque([(i,0)])
            vis=set([i])
            #print(q)
            while q:
                for j in range(len(q)):
                    node,c=q.popleft()
                    if not node.left and not node.right and c>0 and c<=distance :
                        count+=1
                    if c>distance:
                        break
                    if node in d and d[node] not in vis:
                        q.append([d[node],c+1])
                        vis.add(d[node])
                    if node.right and node.right not in vis:
                        q.append([node.right,c+1])
                        vis.add(node.right)
                    if node.left and node.left not in vis:
                        q.append([node.left,c+1])
                        vis.add(node.left)
        return count//2