# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #Time: O(n) since we visit every node
        #Space: O(logn) the call stack only holds half on the values since it's a BST
        
        return convert(nums, 0, len(nums) - 1)
    
def convert(nums, start, end):
    if start > end: return None
    
    middle = (start + end) // 2
    newNode = TreeNode(nums[middle])
    newNode.left = convert(nums, start, middle - 1)
    newNode.right = convert(nums, middle + 1, end)

    return newNode