"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        curr=head
        stack=[]
        while curr or stack:
            if curr:
                #print(curr.val)
                #print(stack)
                if curr.child!=None:
                    if curr.next:
                        stack.append(curr.next)
                    curr.next=curr.child        
                    curr.child=None
                    c=curr
                    curr=curr.next
                    curr.prev=c
                elif curr.child==None and curr.next!=None:
                    curr=curr.next    
                else:  
                    if stack:
                        curr.next=stack.pop()    
                    if curr.next:    
                        c=curr    
                        curr=curr.next        
                        curr.prev=c
                    else:    
                        curr=curr.next 
        return head
        """
        :type head: Node
        :rtype: Node
        """
        