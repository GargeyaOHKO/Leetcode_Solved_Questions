# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1 for i in range(n)] for j in range(m)]
        #print(mat)
        l=[]
        curr=head
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        if len(l)==1:
            mat[0][0]=l[0]
            return mat
        a,b,c,d=0,n,m,-1
        z,i,j=0,0,0
        while z<len(l):
            while j+1<b and z<len(l):
                print(i,j,z)
                mat[i][j]=l[z]
                j+=1
                z+=1
            b-=1
            while i+1<c and z<len(l):
                print(i,j,z)
                mat[i][j]=l[z]
                i+=1
                z+=1
            c-=1
            while j-1>d and z<len(l):
                print(i,j,z)
                mat[i][j]=l[z]
                j-=1
                z+=1
            d+=1
            while i-1>a and z<len(l):
                print(i,j,z)
                mat[i][j]=l[z]
                i-=1
                z+=1
            a+=1
        return mat

                
