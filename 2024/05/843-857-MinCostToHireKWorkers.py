"""
Leetcode
857. Minimum Cost to Hire K Workers
Hard
2024-05-11

There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

    Every worker in the paid group must be paid at least their minimum wage expectation.
    In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.

Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

 

Constraints:

    n == quality.length == wage.length
    1 <= k <= n <= 10^4
    1 <= quality[i], wage[i] <= 10^4
"""

import heapq
from typing import List


class Solution:
    """
    leetcode solution: Priority Queue
    Runtime: 151 ms, faster than 74.48% of Python3 online submissions for Minimum Cost to Hire K Workers.
    Memory Usage: 19 MB, less than 52.82% of Python3 online submissions for Minimum Cost to Hire K Workers.
    """

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        total_cost = float('inf')
        current_total_quality = 0
        wage_to_quality_ratio = [(0, 0)] * n

        # calculate wage-to-quality ratio for each worker
        for i in range(n):
            wage_to_quality_ratio[i] = (wage[i] / quality[i], quality[i])

        # sort workers based on their wage-to-quality ratio
        wage_to_quality_ratio.sort(key=lambda x: x[0])

        # use heap to keep track of the highest quality workers
        highest_quality_workers = []

        for i in range(n):
            heapq.heappush(highest_quality_workers, -
                           wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            # if we have more than k workers,
            # remove the ones with highest quality
            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)

            # if we have exactly k workers,
            # calculate the total cost and update if it's the minimum
            if len(highest_quality_workers) == k:
                total_cost = min(
                    total_cost, current_total_quality *
                    wage_to_quality_ratio[i][0]
                )

        return total_cost
