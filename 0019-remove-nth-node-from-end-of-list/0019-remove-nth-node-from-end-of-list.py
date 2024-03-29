# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length,curr=0,head
        while curr:
            length+=1
            curr=curr.next  
        rem,curr=(length-n+1),head
        index=1
        dum=ListNode()
        newll=dum
        while curr:
            if index==rem:  
                newll.next=curr.next 
                if curr.next==None:
                    curr=curr.next
                else:    
                    curr=curr.next.next     
            else: 
                newll.next=curr
                curr=curr.next    
            newll=newll.next
            index+=1    
        return dum.next        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        