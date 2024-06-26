# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res=[]
        def inorder(res,root):
            if not root:
                return None
            else:
                inorder(res,root.left)
                res.append(root.val)
                inorder(res,root.right)
        inorder(res,root)
        curr=None
        def dfs(low,high):
            if low==high:
                return TreeNode(res[low])
            if low>high:
                return None
            
            mid=(low+high)//2
            curr=TreeNode(res[mid])

            curr.left=dfs(low,mid-1)
            curr.right=dfs(mid+1,high)

            return curr
        return dfs(0,len(res)-1)
            