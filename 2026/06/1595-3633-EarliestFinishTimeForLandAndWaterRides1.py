"""
Leetcode
2026-06-02
3633. Earliest Finish Time for Land and Water Rides I
Easy

You are given two categories of theme park attractions: land rides and water rides.

    Land rides
        landStartTime[i] – the earliest time the ith land ride can be boarded.
        landDuration[i] – how long the ith land ride lasts.
    Water rides
        waterStartTime[j] – the earliest time the jth water ride can be boarded.
        waterDuration[j] – how long the jth water ride lasts.

A tourist must experience exactly one ride from each category, in either order.

    A ride may be started at its opening time or any later moment.
    If a ride is started at time t, it finishes at time t + duration.
    Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the earliest possible time at which the tourist can finish both rides.

 

Example 1:

Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]

Output: 9

Explanation:

    Plan A (land ride 0 → water ride 0):
        Start land ride 0 at time landStartTime[0] = 2. Finish at 2 + landDuration[0] = 6.
        Water ride 0 opens at time waterStartTime[0] = 6. Start immediately at 6, finish at 6 + waterDuration[0] = 9.
    Plan B (water ride 0 → land ride 1):
        Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
        Land ride 1 opens at landStartTime[1] = 8. Start at time 9, finish at 9 + landDuration[1] = 10.
    Plan C (land ride 1 → water ride 0):
        Start land ride 1 at time landStartTime[1] = 8. Finish at 8 + landDuration[1] = 9.
        Water ride 0 opened at waterStartTime[0] = 6. Start at time 9, finish at 9 + waterDuration[0] = 12.
    Plan D (water ride 0 → land ride 0):
        Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
        Land ride 0 opened at landStartTime[0] = 2. Start at time 9, finish at 9 + landDuration[0] = 13.

Plan A gives the earliest finish time of 9.

Example 2:

Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]

Output: 14

Explanation:

    Plan A (water ride 0 → land ride 0):
        Start water ride 0 at time waterStartTime[0] = 1. Finish at 1 + waterDuration[0] = 11.
        Land ride 0 opened at landStartTime[0] = 5. Start immediately at 11 and finish at 11 + landDuration[0] = 14.
    Plan B (land ride 0 → water ride 0):
        Start land ride 0 at time landStartTime[0] = 5. Finish at 5 + landDuration[0] = 8.
        Water ride 0 opened at waterStartTime[0] = 1. Start immediately at 8 and finish at 8 + waterDuration[0] = 18.

Plan A provides the earliest finish time of 14.

 

Constraints:

    1 <= n, m <= 100
    landStartTime.length == landDuration.length == n
    waterStartTime.length == waterDuration.length == m
    1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000


"""

from typing import List


class Solution01:
    """
    Runtime 174ms Beats 51.16%
    Memory 19.32MB Beats 56.98%
    """

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = 1 << 31

        for r1s, r1d in zip(landStartTime, landDuration):
            for r2s, r2d in zip(waterStartTime, waterDuration):
                cur = 0
                if r1s < r2s or (r1s == r2s and r1d < r2d):
                    cur = r1s + r1d
                    cur = max(cur, r2s)
                    cur += r2d
                else:
                    cur = r2s + r2d
                    cur = max(cur, r1s)
                    cur += r1d
                ans = min(ans, cur)

        return ans


class Solution02:
    """
    Runtime 215ms Beats 41.86%
    Memory 19.52MB Beats 5.23%
    """

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = 1 << 31

        for r1s, r1d in zip(landStartTime, landDuration):
            for r2s, r2d in zip(waterStartTime, waterDuration):
                ans = min(ans, max(r1s, r2s + r2d) +
                          r1d, max(r2s, r1s + r1d) + r2d)

        return ans


class Solution1:
    """
    leetcode solution 1: Brute Force Enumeration + Classification Discussion
    Runtime 281ms Beats 16.86%
    Memory 19.40MB Beats 18.02%
    """

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        res = float('inf')
        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                res = min(res, land_water)

                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                res = min(res, water_land)
        return int(res)


class Solution2:
    """
    leetcode solution 2: Linear Enumeration + Classification Discussion
    Runtime 6ms Beats 90.70%
    Memory 19.33MB Beats 56.98%
    """

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(start1, duration1, start2, duration2):
            finish1 = float('inf')
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
            finish2 = float('inf')
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])
            return finish2

        land_water = solve(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_land = solve(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return int(min(land_water, water_land))
