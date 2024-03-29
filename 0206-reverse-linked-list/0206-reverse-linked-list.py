# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev,curr=None,head
        tcurr=curr
        while curr:
            nxt=curr.next
            tcurr=curr
            curr.next=prev
            prev=tcurr
            curr=nxt
        return prev
        """
        :type head: ListNode
        :rtype: ListNode
        """
        