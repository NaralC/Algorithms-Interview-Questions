class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return countCharAndHash(strs)
    
def sortAndHash(strs):
    #Time: O(m * nlog(n)) where m = number of words, n = average word length
    #Space: O(m * n)
    output = {}
    
    for word in strs:
        sortedWord = ''.join(sorted(word))
        
        if sortedWord in output:
            output[sortedWord].append(word)
        else:
            output[sortedWord] = [word]
        
    return output.values()

def countCharAndHash(strs):
    #Time: O(m * n) where m = number of words, n = average word length
    #Space: O(m * n)
    output = {}
    
    for word in strs:
        #Hash tables don't work since casting them to tuples in order to assign them as dict keys will group all values together in one array
        
        charFreq = [0] * 26 #where each idx represents 0-25 English alphabets
        
        for char in word:
            #Eg. ord('a') - ord('a') = 0
            charFreq[ord(char) - ord('a')] += 1
        
        if tuple(charFreq) in output:
            output[tuple(charFreq)].append(word)
        else:
            output[tuple(charFreq)] = [word]
        
            
    return output.values()