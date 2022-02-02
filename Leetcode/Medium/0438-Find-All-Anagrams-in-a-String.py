class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Time: O(s)
        #Space: O(s)
        
        #s must always be longer than p
        if len(s) < len(p): return []
        
        #Set up variables for our first comparison
        s_count, p_count = {}, {}
        
        for idx in range(len(p)):
            s_count[s[idx]] = s_count.get(s[idx], 0) + 1
            p_count[p[idx]] = p_count.get(p[idx], 0) + 1
        
        #Make our first comparison
        output = [0] if s_count == p_count else []
        
        #Use the sliding window technique for further comparisons
        left, right = 0, len(p) - 1
        
        while right < len(s):
            #Remove the left most element of the window from hashtable
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
                
            #Progress ptrs
            left += 1; right += 1
            
            #Add the right most element of the window to hashtable
            if right < len(s):
                s_count[s[right]] = s_count.get(s[right], 0) + 1
            
            #Compare
            if s_count == p_count:
                output.append(left)
                
        return output