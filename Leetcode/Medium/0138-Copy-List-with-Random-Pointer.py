from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time: O(n) two passes
        # Space: O(n) since we're allocating a new list
        
        # Make a property-less copy of the old list, while linking the old ones to their new corresponding ones
        oldToNew = defaultdict(lambda: None)
        old = head
        
        while old:
            oldToNew[old] = Node(old.val)
            
            old = old.next
            
        # Loop over the old list again, and copy all of the properties to the new corresponding one
        old = head
        
        while old:
            new = oldToNew[old]
            new.next = oldToNew[old.next]
            new.random = oldToNew[old.random]
            
            old = old.next
            
        # Ship the new head
        return oldToNew[head]