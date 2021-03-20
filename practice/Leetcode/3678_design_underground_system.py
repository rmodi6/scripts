# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3678/

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.avg = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        source, t1 = self.check_in[id]
        diff = t - t1
        avg, total = self.avg.get((source, stationName), (0, 0))
        self.avg[(source, stationName)] = ((avg*total+diff)/(total+1), total+1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
