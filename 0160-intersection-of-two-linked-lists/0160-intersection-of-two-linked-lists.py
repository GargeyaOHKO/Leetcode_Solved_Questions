# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        s=set()
        curr1=headA
        curr2=headB
        c1,c2=0,0
        while curr1:
            c1+=1
            s.add(curr1)
            curr1=curr1.next
        while curr2:
            c2+=1
            if curr2 in s:
                return curr2
            curr2=curr2.next
        if curr1!=curr2:
            return None        

        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        