"""
Leetcode
502. IPO (hard)
2023-02-23

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
"""

from typing import List, Optional
import heapq


class Solution:
    """
    Wrong Answer
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        q = []
        for p, c in zip(profits, capital):
            # push -p as a workaround to make q a max-heap
            # (heappush makes a min-heap)
            heapq.heappush(q, (-p, c))

        for _ in range(k):

            nxt_project_idx = -1

            for i, (project_profit, project_capital) in enumerate(q):
                if project_capital > w:
                    continue
                nxt_project_idx = i
                break

            if nxt_project_idx < 0:
                break

            nxt_project = q.pop(nxt_project_idx)
            # reverse profit negation that was done while creating q
            w += -nxt_project[0]

        return w


class Solution1:
    """
    leetcode solution
    Runtime: 1151 ms, faster than 41.78% of Python3 online submissions for IPO.
    Memory Usage: 38.9 MB, less than 42.66% of Python3 online submissions for IPO.
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()

        # store negated elements as a workaround for making max-heap
        q = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                # push a negated element
                heapq.heappush(q, -projects[i][1])
                i += 1
            if not q:
                break
            # pop element and reverse negation
            w += -heapq.heappop(q)

        return w


s = Solution1()
tests = [
    ((2, 0, [1, 2, 3], [0, 1, 1]),
     4),

    ((3, 0, [1, 2, 3], [0, 1, 2]),
     6),
]
for inp, exp in tests:
    res = s.findMaximizedCapital(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
