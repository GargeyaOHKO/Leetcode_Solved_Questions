# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import math
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        if head.next==None:
            return head
        curr1=head
        curr2=head.next
        while curr2!=None:
            temp=ListNode(math.gcd(curr1.val,curr2.val))
            curr1.next=temp
            temp.next=curr2
            curr1=curr1.next.next
            curr2=curr2.next
        return head
        