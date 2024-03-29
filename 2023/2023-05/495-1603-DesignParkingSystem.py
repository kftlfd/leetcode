"""
Leetcode
1603. Design Parking System (easy)
2023-05-29

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

    ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
    bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

Example 1:

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
"""

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


class ParkingSystem:
    """
    Runtime: 134 ms, faster than 76.22% of Python3 online submissions for Design Parking System.
    Memory Usage: 16.9 MB, less than 15.89% of Python3 online submissions for Design Parking System.
    """

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        
        if carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        
        if carType == 3 and self.small > 0:
            self.small -= 1
            return True
        
        return False


class ParkingSystem2:
    """
    Runtime: 140 ms, faster than 44.63% of Python3 online submissions for Design Parking System.
    Memory Usage: 16.7 MB, less than 44.25% of Python3 online submissions for Design Parking System.
    """

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            1: big,
            2: medium,
            3: small,
        }
        

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] > 0:
            self.parking[carType] -= 1
            return True
        
        return False
