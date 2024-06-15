# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        fl,l,d=[],[],{}
        self.ans=0
        def dfs(root,l,fl):
            if not root:
                return None
            else:
                if root.val not in d:
                    d[root.val]=1
                else:
                    d[root.val]+=1    
                if not root.left and not root.right:
                    odd=0    
                    for j in d:
                        if d[j]%2!=0:
                            odd+=1
                        if odd>1:
                            break
                    if odd<2:
                        self.ans+=1

                dfs(root.left,l,fl)
                dfs(root.right,l,fl)
            d[root.val]-=1
        dfs(root,[],fl)      
        return self.ans
        """
        :type root: TreeNode
        :rtype: int
        """
        