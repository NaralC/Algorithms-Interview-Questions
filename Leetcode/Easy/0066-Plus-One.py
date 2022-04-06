class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n) since the last case requires append to another array
        
        for idx in reversed(range(len(digits))):
            # Case 1: the number is 9 -> make it 0, and continue
            if digits[idx] == 9:
                digits[idx] = 0
            
            # Case 2: the number is lower than 9 -> increment it by 1 and terminate
            else:
                digits[idx] += 1
                return digits
        
        # Handle cases like [9] and [9, 1]
        return [1] + digits