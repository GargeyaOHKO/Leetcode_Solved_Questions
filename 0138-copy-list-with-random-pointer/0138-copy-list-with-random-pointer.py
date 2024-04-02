"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        d={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            d[curr]=copy
            curr=curr.next

        curr=head
        while curr:
            copy=d[curr]
            copy.next=d[curr.next]
            copy.random=d[curr.random]
            curr=curr.next
        return d[head]        
        """
        :type head: Node
        :rtype: Node
        """
        