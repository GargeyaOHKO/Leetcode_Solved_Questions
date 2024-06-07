# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr=root
        stack=[]
        res=[]
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                res.append(curr.val)
                curr=curr.right
        
        d={}
        s=0
        for i in range(len(res)-1,-1,-1):
            s+=res[i]
            d[res[i]]=s

        curr=root
        stack=[]
        while curr or stack:
            if curr:
                stack.append(curr.right)
                curr.val=d[curr.val]
                curr=curr.left
            else:
                curr=stack.pop()
        return root    
                

        