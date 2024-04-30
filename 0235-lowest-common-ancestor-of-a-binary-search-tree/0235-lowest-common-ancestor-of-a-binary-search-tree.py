# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        res1,res2=[],[]
        curr=root
        flag=True
        while curr and flag:
            res1.append(curr.val)
            if curr.val==p.val:
                break
                flag=False
            elif curr.val>p.val:
                curr=curr.left
            else:
                curr=curr.right
        curr=root       
        while curr:
            res2.append(curr.val)
            if curr.val==q.val:
                break
            elif curr.val>q.val:
                curr=curr.left
            else:
                curr=curr.right   
        ans=0
        for i in range(min(len(res1),len(res2))):
            if res1[i]==res2[i]:
                ans=res1[i]
            else:
                break
        curr=root       
        while curr:
            if curr.val==ans:
                return curr
            elif curr.val>ans:
                curr=curr.left
            else:
                curr=curr.right                                  
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        