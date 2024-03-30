# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dum=ListNode(0,head)
        slow=dum
        fast=head
        while n>0 and fast:
            fast=fast.next
            n-=1    
        while fast:
            slow=slow.next
            fast=fast.next
        if slow.next==None:
            slow.next=None
        else:        
            slow.next=slow.next.next        
        return dum.next    
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        