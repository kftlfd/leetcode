"""
Leetcode
1235. Maximum Profit in Job Scheduling (hard)
2022-11-26

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
"""

from typing import List, Optional
import bisect


# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC++Python-DP-Solution
# Runtime: 1349 ms, faster than 54.79% of Python3 online submissions for Maximum Profit in Job Scheduling.
# Memory Usage: 27.6 MB, less than 61.89% of Python3 online submissions for Maximum Profit in Job Scheduling.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        # zip, sort by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        # dp: [end time, profit]
        dp = [[0, 0]]

        for s, e, p in jobs:
            prev_idx = bisect.bisect(dp, [s+1, 0]) - 1
            if dp[prev_idx][1] + p > dp[-1][1]:
                dp.append([e, dp[prev_idx][1] + p])

        return dp[-1][1]


s = Solution()
tests = [
    (([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]),
     120),

    (([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]),
        150),

    (([1, 1, 1], [2, 3, 4], [5, 6, 4]),
     6)
]
for inp, exp in tests:
    startTime, endTime, profit = inp
    res = s.jobScheduling(startTime, endTime, profit)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
