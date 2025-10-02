class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        stack = [] # contains (char, freq)

        for char in s:
            # Same char
            if len(stack) and stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] >= k: stack.pop()

            # Diff char
            else:
                stack.append([char, 1])

        return ''.join([char * freq for char, freq in stack])
