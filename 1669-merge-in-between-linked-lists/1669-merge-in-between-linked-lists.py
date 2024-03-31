# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        dum=ListNode()
        ll=dum
        c=0
        curr1=list1
        curr2=list2
        while c<a:
            ll.next=curr1
            ll=ll.next
            curr1=curr1.next 
            c+=1    
        ll.next=curr2
        while ll.next!=None:
            ll=ll.next
        while curr1:
            if c<=b:
                curr1=curr1.next
            else:
                ll.next=curr1
                break    
            c+=1    
        return dum.next
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        