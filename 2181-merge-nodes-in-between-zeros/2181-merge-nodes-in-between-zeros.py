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
        while curr.next!=None:
            curr=curr.next
            if curr.val==0:
                l.append(s)
                s=0
            else:
                s+=curr.val
        dummy=ListNode(None)
        head=dummy
        for i in l:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return head.next 
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        