# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        curr,prev=head,None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        #print(prev)
        fhead=ListNode(None)
        curr=fhead
        carry=0
        while prev:
            if carry+prev.val+prev.val>9:
                fhead.next=ListNode(carry+prev.val+prev.val-10)
                carry=1
            else:
                fhead.next=ListNode(carry+prev.val+prev.val)
                carry=0
            prev=prev.next    
            fhead=fhead.next
        if carry:
            fhead.next=ListNode(1)
        curr=curr.next
        prev=None
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
        