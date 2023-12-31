"""
Leetcode
1011. Capacity To Ship Packages Within D Days (medium)
2023-02-22

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

from typing import List, Optional


class Solution:
    """
    leetcode solution
    Runtime: 875 ms, faster than 17.70% of Python3 online submissions for Capacity To Ship Packages Within D Days.
    Memory Usage: 17.1 MB, less than 77.72% of Python3 online submissions for Capacity To Ship Packages Within D Days.
    """

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        max_weight = 0
        total_weight = 0
        for w in weights:
            max_weight = max(max_weight, w)
            total_weight += w

        l = max_weight
        r = total_weight
        while l < r:
            capacity = (l + r) // 2
            if self.canShip(weights, days, capacity):
                r = capacity
            else:
                l = capacity + 1

        return l

    def canShip(self, weights: List[int], days: int, capacity: int) -> bool:
        days_left = days
        curr_load = 0
        i = 0
        l = len(weights)
        while i < l and days_left > 0:
            while i < l and curr_load + weights[i] <= capacity:
                curr_load += weights[i]
                i += 1
            days_left -= 1
            curr_load = 0
        return i == l


s = Solution()
tests = [
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
     15),

    (([3, 2, 2, 4, 1, 4], 3),
     6),

    (([1, 2, 3, 1, 1], 4),
     3),
]
for inp, exp in tests:
    res = s.shipWithinDays(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
