# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #print(ord('a'))
        fl=[]
        self.dfs(root,"",fl)
        #print(fl)
        return min(fl)
    def dfs(self,root,l,fl):
        if not root:
            return None
        else:
            l=chr(root.val+97)+l
            if not root.left and not root.right:
                fl.append(str(l)) 
            self.dfs(root.left,l,fl)
            self.dfs(root.right,l,fl)
        l=l[:len(l)-1]
        return fl    

