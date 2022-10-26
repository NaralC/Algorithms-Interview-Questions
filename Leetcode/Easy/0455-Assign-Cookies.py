class Solution:
    def findContentChildren(self, kids: List[int], cookies: List[int]) -> int:
        # Time: O(nlogn + mlogm)
        # Space: O(1)
        
        kids.sort()
        cookies.sort()
        k = c = output = 0
        
        while k < len(kids) and c < len(cookies):
            # Gratification, move on from this kid and use up current cookie
            if kids[k] <= cookies[c]:
                k += 1; c += 1
                output += 1
            
            # Find a bigger cookie
            else:
                c += 1
        
        return output
        