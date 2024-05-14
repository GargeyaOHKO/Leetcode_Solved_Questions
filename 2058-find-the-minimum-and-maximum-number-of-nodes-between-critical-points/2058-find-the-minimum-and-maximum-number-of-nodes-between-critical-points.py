# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        maxi=0
        mini=float('infinity')
        curr=head.next
        prev=head
        c1=0
        c2=0
        firstflag=False
        while curr.next!=None:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                #print(curr.val)
                if firstflag:
                    mini=min(mini,c2)
                    c2=0
                if not firstflag:
                    firstflag=True
                    c1+=1
                else:
                    maxi=max(maxi,c1)
                c2+=1    
            else:
                c2+=1
                c1+=1
            curr=curr.next
            prev=prev.next    
        if maxi==0:
            return [-1,-1]
        else:
            return [mini,maxi]            