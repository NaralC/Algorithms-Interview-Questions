class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Time: O(?)
        #Space: O(?)
        
        def dfs(combination, currentSum, leftToUse):
            if currentSum > target:
                return
            
            elif currentSum == target:
                output.append(combination)
                return
            
            #Try out every single possibility since the same number can be used over and over
            for idx, num in enumerate(leftToUse):
                dfs(combination + [num], currentSum + num, leftToUse[idx:])
                
        output = []
        dfs([], 0, candidates)
        return output