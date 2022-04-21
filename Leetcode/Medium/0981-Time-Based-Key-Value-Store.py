from collections import defaultdict

class TimeMap:

    # {key : [value, timestamp]}
    # {'foo': [['bar', 1], ['bar2', 4]]}
    
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        output = ''
        pairs = self.data[key]
        
        # Perform binary search to find the closest value to timestamp
        left = 0; right = len(pairs) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found an exact match
            if pairs[mid][1] == timestamp:
                return pairs[mid][0]
            
            # Found a previous timestamp, look for a more recent one
            if pairs[mid][1] < timestamp:
                output = pairs[mid][0]
                left = mid + 1
        
            # Found a future timestamp, look for an older one
            else:
                right = mid - 1
        
        return output


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)