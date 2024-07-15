# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: List[List[int]]) -> Optional[TreeNode]:
        child=set()
        d={}
        for i in desc:
            child.add(i[1])
        for i in desc:
            if i[0] not in child:
                root=i[0]
            if i[2]==1:
                if i[0] not in d:
                    d[i[0]]=["l"+str(i[1])] 
                else:
                    d[i[0]].insert(0,"l"+str(i[1]))
            elif i[2]==0:
                if i[0] not in d:
                    d[i[0]]=["r"+str(i[1])] 
                else:
                    d[i[0]].append("r"+str(i[1]))
        #print(d,child)
        curr=TreeNode(root)
        root=curr
        stack=[]
        while stack or child:
            #print(curr,stack,child)
            if curr and curr.val in d:
                if len(d[curr.val])==2:
                    curr.left=TreeNode(int(d[curr.val][0][1:]))
                    curr.right=TreeNode(int(d[curr.val][1][1:]))
                    child.remove(int(d[curr.val][0][1:]))
                    child.remove(int(d[curr.val][1][1:]))
                    stack.append(curr.right)
                    curr=curr.left
                elif len(d[curr.val])==1:
                    if curr.val in d and d[curr.val][0][0]=="l":
                        curr.left=TreeNode(int(d[curr.val][0][1:]))
                        child.remove(int(d[curr.val][0][1:]))
                        curr=curr.left
                    else:
                        curr.right=TreeNode(int(d[curr.val][0][1:]))
                        child.remove(int(d[curr.val][0][1:]))
                        stack.append(curr.right)
                        curr=curr.left
            else:
                curr=stack.pop()
        return root


        