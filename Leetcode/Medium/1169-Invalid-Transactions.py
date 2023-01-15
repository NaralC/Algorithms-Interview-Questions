class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Time: O(n)
        # Space: O(n)
        
        lookup = dict() # { (name, time): {city1, ...} }
        output = []
        
        # transactions[idx] = valid if either is true:
        # - amount > 1000
        # - occurs within 60 mins in a different city, but same name
        
        for t in transactions:
            name, time, amount, city = t.split(',')
            
            if (name, time) not in lookup: 
                lookup[(name, int(time))] = {city}
            else:
                lookup[(name, int(time))].add(city)
        
        for t in transactions:
            name, time, amount, city = t.split(',')
            # Amount check
            if int(amount) > 1000:
                output.append(t)
                continue
            
            # Time/city overlap check
            for seconds in range(61):
                key1 = (name, int(time) + seconds)
                key2 = (name, int(time) - seconds)
                
                if key1 in lookup and city not in lookup[key1]:
                    output.append(t)
                    break
                    
                if key2 in lookup and city not in lookup[key2]:
                    output.append(t)
                    break
                    
        return output
    