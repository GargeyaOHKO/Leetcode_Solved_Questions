# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2): 
        dum=ListNode()
        curr=dum
        while list1 and list2:
            if list1.val>=list2.val:
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next    
        while list1:
            curr.next=list1
            list1=list1.next
            curr=curr.next
        while list2:
            curr.next=list2
            list2=list2.next
            curr=curr.next               
        return dum.next           
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        