class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Time: O(n)
        #Space: O(n)

        def dfs(combination, currentSum, startIdx):
            if currentSum > target:
                return
            
            elif currentSum == target:
                output.append(combination)
                return
            
            #Try out every single possibility since the same number can be used over and over
            for idx in range(startIdx, len(candidates)):
                dfs(combination + [candidates[idx]], currentSum + candidates[idx], idx)
                
        output = []
        dfs([], 0, 0)
        return output