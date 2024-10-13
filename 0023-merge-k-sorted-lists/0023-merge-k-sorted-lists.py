# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        for i in lists:
            c=i
            #print(c.val)
            while c!=None:
                heapq.heappush(h,c.val)
                c=c.next
        h.sort()
        head=ListNode(None)
        curr=head
        for i in h:
            curr.next=ListNode(i)
            curr=curr.next
        return head.next



        