# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next  

        dum=ListNode()
        ll=dum
        curr=head
        while curr:
            if curr==slow:
                if curr.next==None:
                    ll.next=None
                    curr=curr.next
                else:
                    ll.next=curr.next
                    curr=curr.next.next
            else:
                ll.next=curr
                curr=curr.next
            ll=ll.next
        return dum.next                    
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        