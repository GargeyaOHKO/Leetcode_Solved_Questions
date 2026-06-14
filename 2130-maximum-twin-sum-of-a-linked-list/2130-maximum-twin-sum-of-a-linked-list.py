# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        c=1
        while fast.next.next!=None:
            c+=1
            slow=slow.next
            fast=fast.next.next

        new=ListNode(val=head.val,next=None)
        curr=head
        curr=curr.next
        while curr!=None:
            temp=ListNode(val=curr.val,next=new)
            new=temp
            curr=curr.next
            
        curr=head
        maxi=0
        for i in range(c):
            maxi=max(maxi,new.val+curr.val)
            curr=curr.next
            new=new.next
        return maxi