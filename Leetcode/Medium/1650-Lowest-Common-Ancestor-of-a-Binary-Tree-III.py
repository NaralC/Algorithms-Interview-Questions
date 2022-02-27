"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #Time: O(h)
        #Space: O(1)
        
        #Get the depth of each node
        pDepth = getDepth(p, 0)
        qDepth = getDepth(q, 0)
        
        #Move up the deeper node by depth difference
        diff = abs(pDepth - qDepth)
        
        if pDepth > qDepth:
            for idx in range(diff):
                p = p.parent
        elif pDepth < qDepth:
            for idx in range(diff):
                q = q.parent
        
        #Simultaneously move both nodes up until they meet
        while p != q:
            if p: p = p.parent
            if q: q = q.parent
        
        return p
        
        
def getDepth(node, count):
    #Traverse upwards until we reach the root
    while node.parent:
        node = node.parent
        count += 1
    
    return count
    
    