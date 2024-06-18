"""
Leetcode
826. Most Profit Assigning Work
Medium
2024-06-18

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

    difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
    worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

Every worker can be assigned at most one job, but one job can be completed multiple times.

    For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

 

Constraints:

    n == difficulty.length
    n == profit.length
    m == worker.length
    1 <= n, m <= 10^4
    1 <= difficulty[i], profit[i], worker[i] <= 10^5
"""

from typing import List, Optional


class Solution:
    """
    Wrong answer
    """

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(list(zip(profit, difficulty)))

        def find_max_job_profit(ability: int) -> int:
            start = 0
            end = len(jobs)
            while start < end:
                mid = start + (end - start) // 2
                if jobs[mid][1] <= ability:
                    start = mid + 1
                else:
                    end = mid
            if end == 0:
                return 0
            return jobs[end - 1][0]

        return sum(find_max_job_profit(w) for w in worker)


class Solution1:
    """
    leetcode solution 1: Binary Search and Greedy (Sort by Job Difficulty)
    Runtime: 414 ms, faster than 12.23% of Python3 online submissions for Most Profit Assigning Work.
    Memory Usage: 19.6 MB, less than 56.95% of Python3 online submissions for Most Profit Assigning Work.
    """

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [(0, 0)] + list(zip(difficulty, profit))
        jobs.sort()

        for i in range(len(jobs) - 1):
            jobs[i + 1] = (
                jobs[i + 1][0],
                max(jobs[i][1], jobs[i+1][1]),
            )

        net_profit = 0

        for ability in worker:
            l = 0
            r = len(jobs) - 1
            job_profit = 0
            while l <= r:
                mid = l + (r - l) // 2
                if jobs[mid][0] <= ability:
                    job_profit = max(job_profit, jobs[mid][1])
                    l = mid + 1
                else:
                    r = mid - 1
            net_profit += job_profit

        return net_profit


class Solution3:
    """
    leetcode solution 3: Greedy and Two-Pointers
    Runtime: 353 ms, faster than 25.85% of Python3 online submissions for Most Profit Assigning Work.
    Memory Usage: 19.6 MB, less than 56.95% of Python3 online submissions for Most Profit Assigning Work.
    """

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(list(zip(difficulty, profit)))
        worker = sorted(worker)

        net_profit = 0
        max_profit = 0
        index = 0

        for ability in worker:
            while index < len(difficulty) and ability >= jobs[index][0]:
                max_profit = max(max_profit, jobs[index][1])
                index += 1
            net_profit += max_profit

        return net_profit


class Solution4:
    """
    leetcode solution 4: Memoization
    Runtime: 528 ms, faster than 8.00% of Python3 online submissions for Most Profit Assigning Work.
    Memory Usage: 19.6 MB, less than 56.95% of Python3 online submissions for Most Profit Assigning Work.
    """

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)

        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        # Take maxima of prefixes.

        for i in range(1, maxAbility + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])
        netProfit = 0
        for ability in worker:
            netProfit += jobs[ability]
        return netProfit
