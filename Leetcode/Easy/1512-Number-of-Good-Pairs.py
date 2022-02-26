class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        #Number of repeated integers | Pairs formed
        #1 | 0 pair
        #2 | 1 pair
        #3 | 3 pairs
        #4 | 6 pairs
        #5 | 10 pairs
        #6 | 15 pairs
        #7 | 21 pairs
        #{x} number of repeated integers = left cell + right cell of the row above
        
        #In one pass, track the frequency of and how many pairs the number has formed
        #Should we run into a number already seen, deploy the equation above
        
        freq = dict() #[number of appearances, pairs formed]
        
        for num in nums:
            if num not in freq:
                freq[num] = [1, 0] #Newly added numbers still cannot form a pair 
            
            else:
                freq[num][1] = freq[num][0] + freq[num][1]
                freq[num][0] += 1
        
        
        #Sum up the number of pairs formed by each number
        output = 0
        
        for pair in freq.values():
            output += pair[1]
        
        return output
        