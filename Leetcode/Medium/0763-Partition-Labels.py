class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        lastIdx = {}
        partitions = []
        
        for idx, char in enumerate(s):
            lastIdx[char] = idx
        
        size, end = 0, 0
        for idx, char in enumerate(s):
            size += 1
            end = max(end, lastIdx[char])
            
            if idx == end:
                partitions.append(size)
                size = 0
                
        return partitions