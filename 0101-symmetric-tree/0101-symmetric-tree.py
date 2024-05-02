# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        r=root.right
        l=root.left
        stack1,stack2=[],[]
        while (r or l) or (stack1 or stack2):
            if r or l:
                if (r==None and l!=None) or (l==None and r!=None):
                    return False
                print(r.val,l.val)
                if r.val!=l.val:
                    return False
                stack1.append(r.right)
                stack2.append(l.left)
                r=r.left
                l=l.right
            else:
                r=stack1.pop()
                l=stack2.pop()
        return True                                            
        """
        :type root: TreeNode
        :rtype: bool
        """
        