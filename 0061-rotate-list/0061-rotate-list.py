# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head==None or head.next==None or k==0:
            return head
        length,curr=1,head
        while curr.next!=None:
            curr=curr.next
            length+=1      
        curr.next=head

        k=k%length
        k=length-k
        c=1
        curr=head
        while k>1:
            curr=curr.next
            k-=1
        head=curr.next
        curr.next=None    
        return head       
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        