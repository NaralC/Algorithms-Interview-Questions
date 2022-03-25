from collections import defaultdict
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        return priorityQueue(items)
        
def priorityQueue(items):
    #Time: O(nlogn) inserting each element into a heap costs O(logn) and we have n elements
    #Space: O(n)

    #Put each stud's score into a hash table (up to 5 scores for each stud)
    lookup = defaultdict(list)

    #With the help of heapq library, we:
    for stud, score in items:
        #Push a score into a stud's reservoir 
        heapq.heappush(lookup[stud], score)

        #Remove a score if there're > 5 of them
        if len(lookup[stud]) > 5:
            heapq.heappop(lookup[stud])

    #Ship the output
    output = []

    for stud in lookup:
         output.append([stud, sum(lookup[stud]) // 5])

    return sorted(output)

def bruteForce(items):
    #Time: O(nlogn)
    #Space: O(n)

    #Sort everyone by their id then by their score
    items.sort(key = lambda x: (x[1], x[0]), reverse = True)

    #Get each student's score into a hashtable
    lookup = defaultdict(list)

    for stud, score in items:
        lookup[stud].append(score)

    #Only take the top five marks of each stud and avg them
    output = []

    for stud, score in lookup.items():
        avg = sum(score[:5]) // len(score[:5]) #This is constant since it's at most 5 numbers

        output.append([stud, avg])

    #Return the output sorted by stud ids 
    return sorted(output)

