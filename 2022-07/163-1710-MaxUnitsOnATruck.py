"""
Leetcode
1710. Maximum Units on a Truck (medium)
2022-07-01

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

 - numberOfBoxesi is the number of boxes of type i.
 - numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
"""

from typing import List


# Runtime: 154 ms, faster than 98.02% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.4 MB, less than 83.07% of Python3 online submissions for Maximum Units on a Truck.
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        boxTypes.sort(key=lambda x: (x[1]))
        while boxTypes and truckSize > 0:
            n, u = boxTypes.pop()
            if n < truckSize:
                total += n * u
                truckSize -= n
            else:
                total += truckSize * u
                truckSize = 0
        return total


s = Solution()
tests = [
    ([[5, 10], [2, 5], [4, 7], [3, 9]], 10),
    ([[1, 3], [2, 2], [3, 1]], 4),
]
for t in tests:
    print(t)
    print(s.maximumUnits(t[0], t[1]))
    print()
