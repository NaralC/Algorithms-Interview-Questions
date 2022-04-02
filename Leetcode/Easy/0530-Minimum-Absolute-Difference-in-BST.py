# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        # Turn the BST into an array with inorder traversal
        def toArray(root):
            if not root:
                return

            toArray(root.left)
            nums.append(root.val)
            toArray(root.right)
            
        nums = []
        toArray(root)
        
        # Run a sliding window over the array to scan for minimum abs diff
        minDiff = float('inf')
        
        for idx in range(1, len(nums)):
            left, right = nums[idx - 1], nums[idx]
            
            minDiff = min(minDiff, abs(left - right))
        
        return minDiff