# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if head.next.next==None:
            return [-1,-1]
        maxi=float('-inf')
        mini=float('inf')
        curr=head
        prev=curr
        curr=curr.next
        l=[]
        c=0
        while curr.next!=None:
            if c>0:
                c+=1
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                #print(prev,curr.val)
                if c==0:
                    c=1
                l.append(c)
            prev=curr
            curr=curr.next
        #print(l)
        for i in range(len(l)-1):
            mini=min(mini,l[i+1]-l[i])

        if len(l)<2:
            return [-1,-1]
        else:
            return [mini,l[-1]-l[0]]

        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        