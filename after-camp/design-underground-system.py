class UndergroundSystem:

    def __init__(self):
        self.checkin = dict()
        self.trips = defaultdict(lambda: (0,0))
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin [id] = (stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start , start_time = self.checkin[id]
        
        total_time , count = self.trips[(start,stationName)]
        self.trips[(start,stationName)] = (total_time - start_time + t, count + 1)
    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        N , D = self.trips[(startStation,endStation)]
        return N/D


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)