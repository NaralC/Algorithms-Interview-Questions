class Solution:
    def reformatDate(self, date: str) -> str:
        #Time: O(?)
        #Space: O(?)

        reference = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', 
                     "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', 
                     "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        
        info = date.split(' ')
        year = info[2]
        month = reference[info[1]] 
        date = info[0][:-2]
        if len(date) < 2:
            date = '0' + date
        
        return f'{year}-{month}-{date}'