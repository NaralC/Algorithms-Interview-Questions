from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Time: O(logn + k)
        #Space: O(k)
        
        #Base case
        if k == len(arr):
            return arr
        
        #Use binary search to find the closest numebr to x
        left, right = 0, len(arr) - 1 
        closest_idx = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == x:
                closest_idx = mid
                break
                
            if abs(arr[mid] - x) < abs(arr[closest_idx] - x):
                closest_idx = mid
                
            if arr[mid] > x:
                right = mid - 1
                
            else:
                left = mid + 1
        
        #Deploy two pointers spread from center approach  
        ret = deque([arr[closest_idx]])
        left, right = closest_idx - 1, closest_idx + 1
        
        while len(ret) < k:
            if right >= len(arr) or abs(arr[left]-x) <= abs(arr[right]-x):
                ret.appendleft(arr[left])
                left -= 1
                
            else:
                ret.append(arr[right])
                right += 1
                
        return ret