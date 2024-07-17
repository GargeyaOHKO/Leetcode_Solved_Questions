# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        l=[]
        s=set(to_delete)
        l.append(root)
        def dfs(root):
            if not root:
                return None
            #print(root.val)
            if root.val in s:
                if root.left:
                    l.append(root.left)
                if root.right:
                    l.append(root.right)
            dfs(root.left)
            dfs(root.right)
            #print(root.val)
            if root.left and root.left.val in s:
                root.left=None
            if root.right and root.right.val in s:
                root.right=None
        dfs(root)
        return [k for k in l if k.val not in s]
        