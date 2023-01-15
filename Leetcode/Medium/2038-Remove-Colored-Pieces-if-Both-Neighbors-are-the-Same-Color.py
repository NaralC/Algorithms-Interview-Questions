class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Time: O(n)
        # Space: O(1)

        # This looks like a counting problem; count 'AAA' and 'BBB'
        # Alice goes first

        a = b = 0

        for idx in range(1, len(colors) - 1):
            if colors[idx] == 'A' == colors[idx - 1] == colors[idx + 1]:
                a += 1
            elif colors[idx] == 'B' == colors[idx - 1] == colors[idx + 1]:
                b += 1
        
        return False if a <= b else True