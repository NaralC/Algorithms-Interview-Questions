class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        #[-4,-2,2,4] a = 1, b = 3, c = 5
        #[9, 3, 15, 33] No negative -> middle dip
        
        #[-4,-2,2,4] a = -1, b = 3, c = 5
        #[-23, -5, 7, 1] One negative -> middle peak
        
        #[-4,-2,2,4] a = -1, b = -3, c = 5
        #[1, 7, -5, -23] Two negative -> middle peak
        
        #[-4,-2,2,4] a = -1, b = -3, c = -5
        #[-9, -3, -15, -33] Three negative -> middle peak
        
        #No Negative = middle dip      or    a > 0 = middle dip
        #Yes Negative = middle peak    or    a < 0 = middle peak

        def quadratic(num):
            return (a * pow(num, 2)) + (b * num) + c
        
        output = []
        left, right = 0, len(nums) - 1
        
        while left <= right:        
            leftNum, rightNum = quadratic(nums[left]), quadratic(nums[right])
            
            if a > 0:
                if leftNum > rightNum:
                    output.append(leftNum)
                    left += 1
                else:
                    output.append(rightNum)
                    right -= 1

            else:
                if leftNum < rightNum:
                    output.append(leftNum)
                    left += 1
                else:
                    output.append(rightNum)
                    right -= 1
                    
        return output[::-1] if a > 0 else output
                
