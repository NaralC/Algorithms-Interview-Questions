class Solution:
    def minimumDeletions(self, s: str) -> int:
        return useStack(s) or twoVars(s)
        
def useStack(s):
    # Time: O(n)
    # Space: O(n)

    # Use stack to cancel bad pairs like 'ba' ('a' always comes before 'b')
    stack = []
    delCount = 0

    for char in s:
        if len(stack) and stack[-1] == 'b' and char == 'a':
            stack.pop()
            delCount += 1 # Emulate deleting 'b'

        else:
            stack.append(char)

    return delCount
        
def twoVars(s):
    # Time: O(n)
    # Space: O(1)

    # Use two variables to cancel bad pairs like 'ba' ('a' always comes before 'b')
    countA = countB = delCount = 0

    for char in s:
        if char == 'b':
            countB += 1

        elif char == 'a':
            if countB:
                countB -= 1
                delCount += 1 # Emulate deleting 'b'

    return delCount
        