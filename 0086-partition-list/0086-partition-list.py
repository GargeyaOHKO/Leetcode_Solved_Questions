# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr=head
        lower=ListNode(None)
        lowerhead=lower
        higher=ListNode(None)
        higherhead=higher
        while curr:
            if curr.val<x:
                lower.next=ListNode(curr.val)
                lower=lower.next
            else:
                higher.next=ListNode(curr.val)    
                higher=higher.next
            curr=curr.next
        lower.next=higherhead.next
        return lowerhead.next      