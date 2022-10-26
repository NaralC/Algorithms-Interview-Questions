from collections import defaultdict

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # Time: O(n)
        # Space: O(n)
        
        # Count each name's frequency while adding to output
        freq = defaultdict(int)
        output = []
        
        for n in names:
            # If not already in dict, just add to it and set its freq to 1
            if n not in freq:
                output.append(n)
                
                # Count the latest addition to output
                freq[n] += 1
            
            # If already in dict, find the lowest k possible that f"{name}(k)" can fit into the dict
            else:
                while n + f'({freq[n]})' in freq:
                    freq[n] += 1
                    
                output.append(n + f'({freq[n]})')
            
                # Count the latest addition to output
                freq[n + f'({freq[n]})'] += 1
        
        return output

    # Use a hashset again, so a little more bruteforce, but TLE on LeetCode 🧼

    # def getFolderNames(self, names: List[str]) -> List[str]:
    #     # Time: O(n)
    #     # Space: O(n)
        
    #     # Count each name's frequency while adding to output
    #     seen = set()
    #     output = []
        
    #     for n in names:
    #         # If not already seen, just add to hashset
    #         if n not in seen:
    #             output.append(n)
    #             seen.add(n)
            
    #         # If already seen, find the lowest k possible that f"{name}(k)" can fit into the set
    #         else:
    #             k = 1
                
    #             while n + f'({k})' in seen:
    #                 k += 1
                    
    #             output.append(n + f'({k})')
    #             seen.add(n + f'({k})')
        
    #     return output