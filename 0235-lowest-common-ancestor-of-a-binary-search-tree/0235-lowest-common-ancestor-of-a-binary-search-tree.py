# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        res1,res2=[],[]
        curr1,curr2=root,root
        flag1,flag2=True,True
        while (curr1 or curr2) and (flag1 or flag2):
            if flag1:
                res1.append(curr1.val)
                if curr1.val==p.val:
                    flag1=False
                elif curr1.val>p.val:
                    curr1=curr1.left
                else:
                    curr1=curr1.right
            if flag2:
                res2.append(curr2.val)
                if curr2.val==q.val:
                    flag2=False
                elif curr2.val>q.val:
                    curr2=curr2.left
                else:
                    curr2=curr2.right   
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
        