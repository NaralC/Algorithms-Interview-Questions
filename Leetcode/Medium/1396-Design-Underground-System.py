class UndergroundSystem:

    def __init__(self):
        self.start = dict() #{customer id : check-in time}
        self.time = dict() #{a -> b : [time intervals, number of rides]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.start.pop(id)
        key = (startStation, stationName)
        currentTrip = t - startTime
        
        if key in self.time:
            previousTrips, count = self.time[key]
            self.time[key] = [previousTrips + currentTrip, count + 1]
        else:
            self.time[key] = [currentTrip, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time[(startStation, endStation)][0] / self.time[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)