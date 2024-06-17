# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(left,right):
            if left==right:
                return TreeNode(nums[left])
            if left>right:
                return None
            mid=(left+right)//2
            curr=TreeNode(nums[mid])
            
            curr.left=rec(left,mid-1)
            curr.right=rec(mid+1,right)

            return curr
        return rec(0,len(nums)-1)
