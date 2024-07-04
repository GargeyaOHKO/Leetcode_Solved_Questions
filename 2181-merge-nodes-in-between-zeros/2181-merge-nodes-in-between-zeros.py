# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        curr=head
        l=[]
        s=0
        dummy=ListNode(None)
        dhead=dummy
        while curr.next!=None:
            curr=curr.next
            if curr.val==0:
                dummy.next=ListNode(s)
                dummy=dummy.next
                s=0
            else:
                s+=curr.val
        return dhead.next 
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        