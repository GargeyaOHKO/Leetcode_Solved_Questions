# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if (p==None and q!=None) or (p!=None and q==None):
            return False
        curr1,stack1=p,[]
        curr2,stack2=q,[]
        res1,res2=[],[]
        while curr2 or stack2 or curr1 or stack1:
            if curr1 or curr2:
                if (curr1==None and curr2!=None) or (curr1!=None and curr2==None) or curr1.val!=curr2.val:
                    return False    
                stack1.append(curr1.right)
                stack2.append(curr2.right)
                curr1=curr1.left
                curr2=curr2.left
            else:
                curr1=stack1.pop()
                curr2=stack2.pop()
        return True
               
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        