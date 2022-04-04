class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        
        # left -> smaller number, while right -> bigger number since the input is sorted
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current = numbers[left] + numbers[right]
            
            # Current number too small? Increase it by moving left inwards
            if current < target:
                left += 1
            
            # Current number too big? Decrease it by moving right inwards
            elif current > target:
                right -= 1
            
            # Found the output pair
            else:
                return [left + 1, right + 1]