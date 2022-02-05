class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #Time: O(n)
        #Space: O(n)
        
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        expected_occurences = len(freq.values())
        actual_occurences = len(set(freq.values()))
        
        #If all number of occurences are unique, the output should be 0
        return expected_occurences - actual_occurences == 0