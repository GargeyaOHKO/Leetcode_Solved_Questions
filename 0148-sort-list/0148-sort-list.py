# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if head==None or head.next==None:
            return head
        left=head
        right=self.getMid(head)   
        tmp=right.next
        right.next=None
        right=tmp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)

    def getMid(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow    

    def merge(self,left,right):
        ll=dum=ListNode()
        while left and right:
            if left.val>right.val:
                ll.next=right
                right=right.next
            else:
                ll.next=left
                left=left.next
            ll=ll.next        
        if left:
            ll.next=left
        if right:
            ll.next=right
        return dum.next                  
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        