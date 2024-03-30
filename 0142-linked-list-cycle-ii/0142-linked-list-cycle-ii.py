# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):   
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if fast==None or fast.next==None:
            return None       
        curr=head    
        while curr:
            if curr==slow:
                return curr
            curr=curr.next
            slow=slow.next
        """
        :type head: ListNode
        :rtype: ListNode
        """
        