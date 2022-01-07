class Solution:
    def jump(self, nums: List[int]) -> int:
        #Time: O(m^n) where m = max(nums), n = len(nums)
        #Space: O(m^n)
        def recursion(pos): #TLE
            if pos >= len(nums) - 1:
                return 0
            
            count = float('inf')
            for steps in range(1, nums[pos] + 1):
                count = min(count, 1 + recursion(pos + steps))
                
            return count
        
        #Time: O(n) where n = len(nums)
        #Space: O(1)
        def greedy():
            left, right = 0, 0
            count = 0
            
            #Terminate when we hit the last position
            while right < len(nums) - 1:
                furthest = 0
                
                for steps in range(left, right + 1):
                    furthest = max(furthest, steps + nums[steps])
                
                left = right + 1
                right = furthest
                count += 1
                
            return count
        
        #Pick your functions here
        return greedy()