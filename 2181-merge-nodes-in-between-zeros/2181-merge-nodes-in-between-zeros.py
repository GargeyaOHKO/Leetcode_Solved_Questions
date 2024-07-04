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
        new=head
        while curr.next!=None:
            curr=curr.next
            if curr.val==0 and curr.next==None:
                new.val=s
                new.next=None
            elif curr.val==0:
                new.val=s
                new=new.next
                s=0
            else:
                s+=curr.val
        new.next=None
        return head 
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        