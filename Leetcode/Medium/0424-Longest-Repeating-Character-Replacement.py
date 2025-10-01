class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        output = 0
        l, r = 0, 0
        lookup = defaultdict(int)

        while r < len(s):
            # Added new char!
            lookup[s[r]] += 1

            # Shrink the substring if other frequencies aside from the highest one exceed our replacement quota
            # Check this by subtracting the highest frequency from the length of current substring
            while (r - l + 1 - max(lookup.values())) > k:
                lookup[s[l]] -= 1
                l += 1

            # Update
            output = max(output, r - l + 1)
            r += 1

        return output
