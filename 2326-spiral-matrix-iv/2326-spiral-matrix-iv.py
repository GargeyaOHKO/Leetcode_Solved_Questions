# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1 for i in range(n)] for j in range(m)]
        #print(mat)
        res=[]
        curr=head
        while curr!=None:
            res.append(curr.val)
            curr=curr.next
        if len(res)==1:
            mat[0][0]=res[0]
            return mat
        #print(mat,l)
        l,r,t,b=0,n-1,0,m-1
        z=0
        while l<=r and t<=b:
            for i in range(l,r+1):
                if z<len(res):
                    mat[t][i]=res[z]
                    z+=1
            t+=1
            for i in range(t,b+1):
                if z<len(res):
                    mat[i][r]=res[z]
                    z+=1
            r-=1
            for i in range(r,l-1,-1):
                if z<len(res):
                    mat[b][i]=res[z]
                    z+=1
            b-=1
            for i in range(b,t-1,-1):
                if z<len(res):
                    mat[i][l]=res[z]
                    z+=1
            l+=1

        return mat