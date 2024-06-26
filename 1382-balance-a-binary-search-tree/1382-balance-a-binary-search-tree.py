# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        curr,stack=root,[]
        res=[]
        while curr or stack:
            #print(stack)
            if curr:
                stack.append(curr)
                curr=curr.left    
            else:
                curr=stack.pop()
                res.append(curr.val)
                curr=curr.right
        print(res)
        curr=None
        def dfs(low,high):
            if low==high:
                return res[low]
            if low>high:
                return None
            
            mid=(low+high)//2
            curr=TreeNode(res[mid])
            
            curr.left=TreeNode(dfs(low,mid-1))
            curr.right=TreeNode(dfs(mid+1,high))

            return curr
        return dfs(0,len(res)-1)
            