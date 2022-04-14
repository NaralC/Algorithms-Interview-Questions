class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n * n!)
        # Space: O(n * n!)
        
        def permute(leftToUse, current):
            if not len(leftToUse):
                output.append(current)
                return
            
            # Attach a char to the current permutation once and remove it
            for idx, char in enumerate(leftToUse):
                permute(leftToUse[:idx] + leftToUse[idx + 1:], current + [char])
                
        output = []
        permute(nums, [])
        return output