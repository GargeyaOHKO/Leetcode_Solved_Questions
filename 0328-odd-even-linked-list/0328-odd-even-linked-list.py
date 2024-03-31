# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):   
        if head==None:
            return None
        c=1
        curr=head
        dum1,dum2=ListNode(),ListNode()
        odd,even=dum1,dum2
        while curr:
            if c%2!=0:
                odd.next=ListNode(curr.val)
                odd=odd.next
            else:   
                even.next=ListNode(curr.val)
                even=even.next 
            curr=curr.next
            c+=1
        curr=dum1.next    
        while curr.next!=None:
            curr=curr.next 
        curr.next=dum2.next
        return dum1.next    

        """
        :type head: ListNode
        :rtype: ListNode
        """
        