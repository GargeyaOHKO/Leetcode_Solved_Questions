# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        curr,c,odd=head,0,False
        while curr!=None:
            c+=1
            curr=curr.next
        if c==1:
            return head
        l,last=[],head
        if c%2!=0:
            while last.next!=None:
                last=last.next
        if c%2!=0:
            odd=True
            c-=1
        curr,count=head,0
        while count!=c:
            prev=None
            for i in range(2):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
                count+=1
            l.append(prev)
        final=ListNode(None)
        head=final
        for i in l:
            final.next=i
            while final.next!=None:
                final=final.next
        if odd:
            final.next=last
        return head.next
        """
        :type head: ListNode
        :rtype: ListNode
        """
        