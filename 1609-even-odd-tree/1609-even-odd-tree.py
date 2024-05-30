# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        q=deque()
        q.append(root)
        fl=[]
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                fl.append(l)
        c=0
        for i in fl:
            if len(i)==1:
                if c%2==0:
                    if i[0]%2==0:
                        return False
                else:                    
                    if i[0]%2!=0:
                        return False
            else:    
                for j in range(len(i)-1):
                    if c%2==0:
                        if i[j]%2==0 or i[j+1]%2==0 or i[j]>=i[j+1]:
                            return False
                    else:                    
                        if i[j]%2!=0 or i[j+1]%2!=0 or i[j]<=i[j+1]:
                            return False
            c+=1            
        return True                
        """
        :type root: TreeNode
        :rtype: bool
        """
        