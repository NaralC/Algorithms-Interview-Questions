class UndergroundSystem:

    def __init__(self):
        self.customer_travel = dict() # { id : {start_station, check_in_time}, ... }
        self.avg_time = dict() # { (start, end) : [total_time, num_of_trips] }

    def checkIn(self, id: int, start: str, t: int) -> None:
        self.customer_travel[id] = (start, t)

    def checkOut(self, id: int, end: str, t: int) -> None:
        start, check_in_time = self.customer_travel[id]
        
        if (start, end) not in self.avg_time:
            self.avg_time[(start, end)] = [t - check_in_time, 1]
        else: 
            self.avg_time[(start, end)][0] += (t - check_in_time)
            self.avg_time[(start, end)][1] += 1

    def getAverageTime(self, start: str, end: str) -> float:
        return self.avg_time[(start, end)][0] / self.avg_time[(start, end)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)