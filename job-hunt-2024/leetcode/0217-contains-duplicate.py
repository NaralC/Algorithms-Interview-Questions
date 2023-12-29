class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(n)

        # Have a hashset keep track of seen elements
        seen = set()

        # Run through the list, look for duplicates
        for n in nums:
            if (n in seen): return True

            seen.add(n)

        return False