class UndergroundSystem:

    def __init__(self):
        # info = [] # stationname, time
        self.data = {}
        self.travel = collections.defaultdict(lambda : [0, 0])
         
         
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        start_info = (stationName, t)
        self.data[id] = start_info

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.data.pop(id)
        self.travel[(start_station, stationName)][0] += (t - start_time)
        self.travel[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.travel[(startStation, endStation)]
        return total_time / total_trips
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
