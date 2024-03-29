# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        second=slow.next
        slow.next=None    
        prev,curr=None,second
        while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt

        first,second=head,prev      
        while first and second:
            t1,t2=first.next,second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
