# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        final=ListNode(None)
        head1=final 

        maxval=prev.val
        while prev:
            if prev.val>=maxval:
                final.next=ListNode(prev.val)
                final=final.next
                maxval=prev.val
            prev=prev.next   

        prev=None
        curr=head1.next
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt      
        return prev


        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        