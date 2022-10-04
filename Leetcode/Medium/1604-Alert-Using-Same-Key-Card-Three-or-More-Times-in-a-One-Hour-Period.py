from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # Time: O(nlogn)
        # Space: O(n)
        # n = either len(keyName) or len(keyTime)
        
        # Put names and times into a hashtable
        count = defaultdict(list)
        
        for name, time in zip(keyName, keyTime):
            count[name].append(getMinutes(time))
        
        # Use a sliding window of size 3 to check the first and last element in it
        output = []
        
        for name, times in count.items():
            if len(times) < 3:
                continue
                
            times.sort()
            
            for idx in range(len(times) - 2):
                first, third = times[idx], times[idx + 2]
                
                if first + 60 >= third:
                    output.append(name)
                    break
            
        return sorted(output)
    
    
def getMinutes(t):
    t = t.split(':')
    hr, mi = t[0], t[-1]
    
    return int(hr) * 60 + int(mi)