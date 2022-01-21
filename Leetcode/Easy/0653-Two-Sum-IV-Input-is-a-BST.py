# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #Time: O(n)
        #Space: O(n)
        #Both BFS and DFS share the same complexity, but don't utilize the fact that the tree is a BST
        #Should come back later
        
        def dfs(root, seen):
            if not root: return False
            
            if k - root.val in seen:
                return True
            seen.add(root.val)
            
            return dfs(root.left, seen) or dfs(root.right, seen)
        
        def bfs(root, seen):
            queue = [root]
            current = None
            
            while queue:
                popped = queue.pop(0)
                
                if k - popped.val in seen:
                    return True
                seen.add(popped.val)
                
                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)
        
        # return dfs(root, set())
        return bfs(root, set())