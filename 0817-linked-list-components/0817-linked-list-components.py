# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        s=set(nums)
        curr=head   
        c=0
        while curr!=None:
            if curr.val not in s:
                c+=1
                flag=False
            else:
                flag=True
            curr=curr.next
        if flag==False:
            return c
        else:
            return c+1
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        