"""
Leetcode
502. IPO
Hard
2024-06-15

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6

 

Constraints:

    1 <= k <= 10^5
    0 <= w <= 10^9
    n == profits.length
    n == capital.length
    1 <= n <= 10^5
    0 <= profits[i] <= 10^4
    0 <= capital[i] <= 10^9
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Runtime: 3857 ms, faster than 5.02% of Python3 online submissions for IPO.
    Memory Usage: 42 MB, less than 14.28% of Python3 online submissions for IPO.
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []

        for prof, cap_req in zip(profits, capital):
            heappush(heap, (-prof, cap_req))

        cur_cap = w

        for _ in range(k):
            if not heap:
                break

            heap2 = []

            prof, cap_req = heappop(heap)

            while cur_cap < cap_req and heap:
                heap2.append((prof, cap_req))
                prof, cap_req = heappop(heap)

            if cur_cap < cap_req:
                break

            cur_cap += -prof

            for v in heap2:
                heappush(heap, v)

        return cur_cap


class Solution1:
    """
    leetcode solution
    Runtime: 707 ms, faster than 70.95% of Python3 online submissions for IPO.
    Memory Usage: 41 MB, less than 83.94% of Python3 online submissions for IPO.
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(list(zip(capital, profits)))

        # store negated elements as a workaround for making max-heap
        q = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                # push a negated element
                heappush(q, -projects[i][1])
                i += 1
            if not q:
                break
            # pop element and reverse negation
            w += -heappop(q)

        return w
