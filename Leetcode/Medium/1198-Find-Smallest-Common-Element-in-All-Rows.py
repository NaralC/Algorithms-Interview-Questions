class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        return hashTable(mat)
        
def utilize_binary_search(mat):
    #Time: O(n * m * logn)
    #Space: O(1)

    def binarySearch(array, target):
        left, right = 0, len(array) - 1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid - 1
            else:
                return True

        return False
    
    #Loop through all elements in the first subarray
    for candidate in mat[0]:
        count = 1

        #Scan other subarrays if the candidate appears in all of them. If yes -> return it
        for array in mat[1:]:
            if binarySearch(array, candidate):
                count += 1

        if count == len(mat):
            return candidate

    return -1


def hashTable(mat):
    #Time: O(m * n)
    #Space: O(m * n)

    #Get how frequent each element appears first
    freq = dict()

    for array in mat:
        for element in array:
            freq[element] = freq.get(element, 0) + 1

    #Only look at numbers that appear in all subarrays, in other words, have a frequency of len(mat)
    candidates = [key for key, value in freq.items() if value == len(mat)]

    return min(candidates) if len(candidates) else -1

