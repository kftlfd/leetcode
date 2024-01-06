"""
Leetcode
1235. Maximum Profit in Job Scheduling
Hard
2024-01-06

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

 

Constraints:

    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    1 <= startTime[i] < endTime[i] <= 10^9
    1 <= profit[i] <= 10^4

    
Hints
- Think on DP.
- Sort the elements by starting time, then define the dp[i] as the maximum profit taking elements from the suffix starting at i.
- Use binarySearch (lower_bound/upper_bound on C++) to get the next index for the DP transition.
"""

from typing import List
from bisect import bisect_left


class Solution:
    """
    Runtime: 1698 ms, faster than 5.03% of Python3 online submissions for Maximum Profit in Job Scheduling.
    Memory Usage: 32.8 MB, less than 43.40% of Python3 online submissions for Maximum Profit in Job Scheduling.
    """

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        mp = []  # max_profit (I,S,P)[]
        I = 0  # index
        S = 1  # start
        P = 2  # profit

        def get(start: int) -> tuple[int, int, int]:
            idx = bisect_left(mp, start, key=lambda x: x[0])
            if idx >= len(mp):
                return [idx, -1, 0]
            return [idx, mp[idx][0], mp[idx][1]]

        for start, end, prof in sorted(zip(startTime, endTime, profit), key=lambda x: -x[0]):
            if not mp:
                mp.append((start, prof))
                continue

            start_mp = get(start)
            end_mp = get(end)

            max_prof = max(
                start_mp[P],
                prof + (end_mp[P] if end_mp[S] >= end else 0)
            )

            if start_mp[S] == start:
                mp[start_mp[I]] = (start, max_prof)
            else:
                mp.insert(start_mp[I], (start, max_prof))

        return get(0)[P]


s = Solution()
tests = [
    (([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]),
     120),

    (([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]),
     150),

    (([1, 1, 1], [2, 3, 4], [5, 6, 4]),
     6),
]
for inp, exp in tests:
    res = s.jobScheduling(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
