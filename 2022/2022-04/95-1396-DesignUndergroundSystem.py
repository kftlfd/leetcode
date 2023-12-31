"""
Leetcode
1396. Design Underground System (medium)
2022-04-24

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

    void checkIn(int id, string stationName, int t)
        A customer with a card ID equal to id, checks in at the station stationName at time t.
        A customer can only be checked into one place at a time.
    void checkOut(int id, string stationName, int t)
        A customer with a card ID equal to id, checks out from the station stationName at time t.
    double getAverageTime(string startStation, string endStation)
        Returns the average time it takes to travel from startStation to endStation.
        The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
        The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
        There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
"""

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)



# try 1
# Runtime: 325 ms, faster than 47.87% of Python3 online submissions for Design Underground System.
# Memory Usage: 24 MB, less than 73.03% of Python3 online submissions for Design Underground System.
class UndergroundSystem:

    def __init__(self):
        self.checkedin = {}
        self.avgtime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        p = self.checkedin.pop(id)
        start = p[0]
        start_time = p[1]
        end = stationName
        end_time = t
        
        if start not in self.avgtime:
            self.avgtime[start] = {}
        if end not in self.avgtime[start]:
            self.avgtime[start][end] = []
            
        self.avgtime[start][end] += [float(end_time - start_time)]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        l = self.avgtime[startStation][endStation]
        return sum(l) / len(l)



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
