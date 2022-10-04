from collections import defaultdict

class Solution:
    def subdomainVisits(self, domains: List[str]) -> List[str]:
        # Time: O(nm)
        # Sapce: O(n)
        # Where n = len(domains), m = length of each subdomain
        
        count = defaultdict(int)

        for d in domains:
            freq, d = d.split(' ')
            freq = int(freq)
            
            count[d] += freq
            
            for idx in range(len(d)):
                if d[idx] == '.':
                    count[d[idx + 1:]] += freq


        return [f"{freq} {domain}" for domain, freq in count.items()]