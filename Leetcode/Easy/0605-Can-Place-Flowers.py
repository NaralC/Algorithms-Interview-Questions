class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        for idx in range(len(flowerbed)):
            if not n:
                break
            
            left = flowerbed[idx - 1] if idx > 0 else None
            right = flowerbed[idx + 1] if idx < len(flowerbed) - 1 else None
            
            if not flowerbed[idx] and not left and not right:
                flowerbed[idx] = 1
                n -= 1
                
        return n == 0