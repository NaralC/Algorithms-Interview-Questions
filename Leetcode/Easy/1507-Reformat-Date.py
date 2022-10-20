class Solution:
    def reformatDate(self, date: str) -> str:
        # Time: O(1)
        # Space: O(1)
        
        # Init hashtable to lookup months
        month_lookup = dict()
        idx = 1
        
        for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
            month_lookup[month] = '0' + str(idx) if idx < 10 else str(idx)
            idx += 1
        
        # Split and ship the output
        day, mon, yr = date.split(' ')
        day = day[:2] if len(day) > 3 else '0' + day[:1]
        
        return f'{yr}-{month_lookup[mon]}-{day}'