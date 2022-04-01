class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return greedy(s)
        
def utilizeStack(s):
    # Time: O(n)
    # Space: O(n)
    
    stack = []

    for idx in reversed(range(len(s))):
        char = s[idx]

        stack.append(char)

        if len(stack) >= 2 and stack[-1] == '(' and stack[-2] == ')':
            stack.pop()
            stack.pop()

    return len(stack)
        
def greedy(s):
    # Time: O(n)
    # Space: O(1)

    unmatchedOpen = unmatchedClose = 0
    output = 0

    for char in s:
        # Require a closing
        if char == '(':
            unmatchedOpen += 1

        # Require an opening
        else:
            # There's an opening already available
            if unmatchedOpen >= 1:
                unmatchedOpen -= 1 # Use it up to make a valid pair
            # There's no opening available
            else:
                unmatchedClose += 1

    return unmatchedOpen + unmatchedClose