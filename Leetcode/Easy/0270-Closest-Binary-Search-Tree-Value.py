# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Time: O(logn)
        # Space: O(1)
        
        closest = float('inf')
        
        while root:
            # Update output
            closest = min(closest, root.val, key = lambda x: abs(target - x))
            
            # Go with the side that is closer to the target
            if target < root.val:
                root = root.left
            else:
                root = root.right
                  
        return closest