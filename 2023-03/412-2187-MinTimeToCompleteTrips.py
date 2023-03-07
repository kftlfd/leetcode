"""
Leetcode
2187. Minimum Time to Complete Trips (medium)
2023-03-07

You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

Example 1:
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

Example 2:
Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.
"""

from typing import List


class Solution:
    """
    Runtime: 1908 ms, faster than 83.25% of Python3 online submissions for Minimum Time to Complete Trips.
    Memory Usage: 28.4 MB, less than 96.75% of Python3 online submissions for Minimum Time to Complete Trips.
    """

    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def possible(time_to_check: int) -> bool:
            trips = 0
            for t in time:
                trips += time_to_check // t
            return trips >= totalTrips

        l = 0  # min time needed
        r = min(time) * totalTrips  # max time needed

        # binary search for time at which neede numer of trips starts to be possible
        while l < r:
            m = (l + r) // 2
            if possible(m):
                r = m
            else:
                l = m + 1

        return r


s = Solution()
tests = [
    (([5, 10, 10], 9),
     25),

    (([1, 2, 3], 5),
     3),

    (([2], 1),
     2),
]
for inp, exp in tests:
    res = s.minimumTime(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
