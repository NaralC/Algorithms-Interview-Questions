class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return countCharAndHash(strs)

def countCharAndHash(strs):
    #Time: O(m * n) where m = number of words, n = average word length
    #Space: O(m * n)
    output = {}
    
    for word in strs:
        count = [0] * 26 #Counting the frequency of each alphabets
        
        for char in word:
            #ord('a') = 97 -> ord('a') - 97 = 0
            count[ord(char) - 97] += 1
        
        if tuple(count) in output:
            output[tuple(count)].append(word)
        else:
            output[tuple(count)] = [word]
            
    return output.values()
    
def sortAndHash(strs):
    #Time: O(m * nlog(n)) where m = number of words, n = length of the longest word
    #Space: O(m * n)
    output = {}

    for word in strs:
        sortedWord = ''.join(sorted(word))

        if sortedWord in output:
            output[sortedWord].append(word)
        else:
            output[sortedWord] = [word]

    return output.values()