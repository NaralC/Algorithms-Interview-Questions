class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Time: O(n)
        # Space: O(1)
        
        window = sum(arr[:k])
        output = 1 if window / k >= threshold else 0
        
        for idx in range(k, len(arr)):
            # Remove the left most element
            window -= arr[idx - k]
            
            # Add a new element
            window += arr[idx]
            
            # Update output
            output += 1 if window / k >= threshold else 0
            
        return output