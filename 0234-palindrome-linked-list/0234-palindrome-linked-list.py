# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        dum=ListNode()
        ll=dum
        curr=head
        while curr:
            ll.next=curr
            curr=curr.next
            ll=ll.next
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt  
        curr=dum.next
        while prev and curr:    
            if prev.val!=curr.val:
                return False
            prev=prev.next
            curr=curr.next
        return True    
        """
        :type head: ListNode
        :rtype: bool
        """
        