# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        c,curr=0,head
        while curr:
            c+=1
            curr=curr.next
        if c%2==0:
            mid=(c//2)+1
        else:
            mid=(c//2)+1
        dum=ListNode()
        ll=dum
        c,curr=1,head
        while curr:
            if c==mid:
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
            c+=1
        return dum.next                    
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        