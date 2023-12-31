"""
Leetcode
983. Minimum Cost For Tickets (medium)
2023-03-28

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

    a 1-day pass is sold for costs[0] dollars,
    a 7-day pass is sold for costs[1] dollars, and
    a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

    For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
"""

from typing import List
from functools import lru_cache


class Solution:
    """
    leetcode solution 1: Dynamic Programming (Day Variant)
    Runtime: 58 ms, faster than 25.65% of Python3 online submissions for Minimum Cost For Tickets.
    Memory Usage: 15.2 MB, less than 9.42% of Python3 online submissions for Minimum Cost For Tickets.
    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)


class Solution1:
    """
    leetcode solution 2: Dynamic Programming (Window Variant)
    Runtime: 52 ms, faster than 43.38% of Python3 online submissions for Minimum Cost For Tickets.
    Memory Usage: 14.4 MB, less than 37.32% of Python3 online submissions for Minimum Cost For Tickets.
    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):  # How much money to do days[i]+
            if i >= N:
                return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)


s = Solution1()
tests = [
    (([1, 4, 6, 7, 8, 20], [2, 7, 15]),
     11),

    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]),
     17),
]
for inp, exp in tests:
    res = s.mincostTickets(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
