# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        c=1
        new=ListNode(val=head.val,next=None)
        while fast.next.next!=None:
            c+=1
            slow=slow.next
            fast=fast.next.next
            temp=ListNode(val=slow.val,next=new)
            new=temp
        slow=slow.next

        maxi=0
        while slow!=None:
            maxi=max(maxi,slow.val+new.val)
            new=new.next
            slow=slow.next
        return maxi