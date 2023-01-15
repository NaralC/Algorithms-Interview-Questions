"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time: O(n)
        # Space: O(n)
        
        if not head: return
        
        stack = []
        dummy = Node('dummy', None, head, None)
        
        while head:
            # Severe connection with next node and connect 2-way with child
            if head.child:
                nxtNode = head.next
                if nxtNode: 
                    stack.append(nxtNode)
                    nxtNode.prev = None
                
                head.next = head.child
                head.child.prev = head
                head.child = None
            
            # Prevent going into None
            if head.next: head = head.next
            else: break
        
        while len(stack):
            head.next = stack.pop()
            head.next.prev = head
            
            while head.next:
                head = head.next
        
        return dummy.next
        