# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        #Time: O(n) as we're visiting all nodes
        #Space: O(n)
        
        traverse(root, '', output := [0])
        return output[0]
        
def traverse(root, current, output):
    if not root:
        return 0
    
    if root and not root.left and not root.right:
        current += str(root.val)
        output[0] += binaryToDecimal(current)
        return

    current += str(root.val)
    
    left = traverse(root.left, current, output)
    right = traverse(root.right, current, output)
    
def binaryToDecimal(binary):
    output, multiplier = 0, 0
    binary = list(binary)
    
    #101 -> 5
    #(1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 5
    while len(binary):
        output += int(binary.pop()) * pow(2, multiplier)
        multiplier += 1
    
    return output