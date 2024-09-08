# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        new=[]
        l=[]
        tl=[0]*k
        length=0
        curr=head
        while curr!=None:
            new.append(curr.val)
            curr=curr.next
            length+=1
        for i in range(length):
            tl[i%k]+=1
        curr=head
        j=0
        #print(new)
        for i in tl:
            node=ListNode(None)
            head=node

            for z in range(i):
                node.next=ListNode(new[j])
                node=node.next
                j+=1
            l.append(head.next)
        return l