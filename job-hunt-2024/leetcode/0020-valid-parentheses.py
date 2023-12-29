class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(n)

        # Must meet their counterpart when popped
        stack = []
        map = { 
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for char in s:
            # If char's a closing piece
            if char not in map:
                if len(stack) < 1: return False # Nothing to check against
                if map[stack.pop()] != char: return False

            # If char's an opening piece
            else:
                stack.append(char)

        if len(stack) > 0: return False
        return True