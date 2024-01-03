class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(logn)
        # Space: O(1)
        # Find the pivot of the rotation -> search on the appropriate side
        
        def findMin():
            lo, hi = 0, len(nums) - 1

            while lo <= hi:
                mid = (lo + hi) // 2

                # Found the pivot; it is to the right of a bigger number
                if nums[mid] > nums[mid + 1]:
                    return mid + 1

                # Mid is on the right side, continue scanning the left
                if nums[lo] > nums[mid]:
                    hi = mid - 1

                # Mid is on the left side, continue scanning the right
                else:
                    lo = mid + 1

            return -1 # This shouldn't happen

        def binarySearch(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                guess = nums[mid]

                if guess == target:
                    return mid

                if guess > target:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return -1

        # If the array is already sorted or has a length of 1
        if nums[0] < nums[-1] or len(nums) == 1:
            return binarySearch(0, len(nums) - 1)

        pivot = findMin()

        # Search right side
        if nums[0] > target:
            return binarySearch(pivot, len(nums) - 1)
        else:
            return binarySearch(0, pivot - 1)
        