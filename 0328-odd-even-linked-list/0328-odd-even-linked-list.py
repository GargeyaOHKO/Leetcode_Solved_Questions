# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):   
        if head==None:
            return None
        last,length=head,1
        while last.next!=None:
            last=last.next
            length+=1    
        end=last.val
        c,curr=1,head
        while c<=(length//2):
            last.next=ListNode(curr.next.val)
            curr.next=curr.next.next
            last=last.next
            curr=curr.next    
            c+=1
        return head       
        """
        :type head: ListNode
        :rtype: ListNode
        """
        