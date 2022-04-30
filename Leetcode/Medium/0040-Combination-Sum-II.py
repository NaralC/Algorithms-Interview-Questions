class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(2^n)
        # Space: O(2^n)
        
        # Brute force and stop when running sum exceeds target
        def dfs(runningSum, path, start):
            if runningSum == target:
                output.append(path)
                
            if runningSum < target:
                for idx in range(start, len(candidates)):
                    # Avoid using a duplicate number
                    if idx > start and candidates[idx] == candidates[idx - 1]:
                        continue
                        
                    dfs(runningSum + candidates[idx], path + [candidates[idx]], idx + 1)
        
        output = []
        candidates.sort() # To deal with cases like [1,7,1] -> [1,1,7]
        dfs(0, [], 0)
        return output