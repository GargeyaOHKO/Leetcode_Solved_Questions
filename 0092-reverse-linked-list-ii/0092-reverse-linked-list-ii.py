# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        final=ListNode(None)
        finalhead=final
        curr=head
        c=1
        prev=None
        while curr:
            if c<left:
                final.next=ListNode(curr.val)
                final=final.next
                curr=curr.next
            elif c>=left and c<=right:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            else:
                break   
            c+=1    
        final.next=prev
        while final.next!=None:
            final=final.next
        final.next=curr           
        return finalhead.next    
    


        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        