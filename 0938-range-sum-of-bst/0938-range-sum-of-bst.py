# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack=[]
        curr=root
        s=0
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                if curr.val>=low and curr.val<=high:
                    s+=curr.val
                if curr.val>high:
                    break    
                curr=curr.right
        return s        

