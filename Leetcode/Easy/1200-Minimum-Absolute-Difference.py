class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #Time: O(nlogn)
        #Space: O(n)
        
        #Check for the lowest abs diff by being greedy
        arr.sort()
        minDiff = float('inf')
        
        for idx in range(1, len(arr)):
            prev, curr = arr[idx - 1], arr[idx]
            
            minDiff = min(minDiff, abs(prev - curr))
        
        #Curate pairs that share the lowest abs diff
        output = []
        
        for idx in range(1, len(arr)):
            prev, curr = arr[idx - 1], arr[idx]
            
            if minDiff == abs(prev - curr):
                output.append([prev, curr])
                
        return output