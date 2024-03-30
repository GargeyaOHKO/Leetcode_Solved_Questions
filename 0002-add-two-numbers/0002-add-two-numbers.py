# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prev1=l1
        prev2=l2
        dum=ListNode()
        ll=dum
        carry=0
        while prev1 or prev2:            
            n1=prev1.val if prev1 else 0
            n2=prev2.val if prev2 else 0
            if n1+n2+carry<10:
                ll.next=ListNode(n1+n2+carry)
                carry=0
            else:
                ll.next=ListNode((n1+n2+carry)-10)
                carry=1
            if prev1!=None:
                prev1=prev1.next
            if prev2!=None:
                prev2=prev2.next    
            ll=ll.next       
        if carry==1:
            ll.next=ListNode(1)
            ll=ll.next
        return dum.next            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        