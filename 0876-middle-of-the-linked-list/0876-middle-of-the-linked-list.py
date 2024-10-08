# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow,fast=head,head
        while head and head.next:
            slow=slow.next
            head=head.next.next
        return slow    
        """
        :type head: ListNode
        :rtype: ListNode
        """
        