# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head==None:
            return head
        length,curr=0,head
        while curr:
            curr=curr.next
            length+=1
        if k%length==0:
            return head    
        shift=k%length
        c=0
        currhead=head
        while c<(length-shift):
            currhead=currhead.next
            c+=1
        returncurr=currhead    
        c=0
        curr=head
        while c<(length-shift):
            if c==(length-shift-1):
                curr.next=None
            c+=1   
            curr=curr.next
        while currhead!=None and currhead.next!=None:    
            currhead=currhead.next      
        if currhead!=None:
            currhead.next=head
        return returncurr
             

            
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        