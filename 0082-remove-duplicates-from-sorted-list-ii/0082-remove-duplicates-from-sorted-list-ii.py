# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr=head
        d={}
        while curr:
            d[curr.val]=d.get(curr.val,0)+1
            curr=curr.next
        curr=head
        New=ListNode(None)
        NewHead=New
        while curr:
            if d[curr.val]==1:
                New.next=ListNode(curr.val)
                New=New.next
            curr=curr.next
        return NewHead.next            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        