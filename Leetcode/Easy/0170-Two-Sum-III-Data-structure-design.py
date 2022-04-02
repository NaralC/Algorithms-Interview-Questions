class TwoSum:
    # Time: O(n)
    # Space: O(n)
    
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        # Run a linear scan to find a potential pair
        seen = set()
        
        for num in self.nums:
            diff = value - num
            
            if diff in seen:
                return True
            seen.add(num)
        
        return False
        

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)