"""
Leetcode
2462. Total Cost to Hire K Workers (medium)
2023-06-26

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

    You will run k sessions and hire exactly one worker in each session.
    In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
        For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
        In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
    If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
    A worker can only be chosen once.

Return the total cost to hire exactly k workers.

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Constraints:

    1 <= costs.length <= 10^5
    1 <= costs[i] <= 10^5
    1 <= k, candidates <= costs.length
"""

from typing import List
import heapq


class Solution:
    """
    Runtime: 2127 ms, faster than 5.10% of Python3 online submissions for Total Cost to Hire K Workers.
    Memory Usage: 27.1 MB, less than 62.15% of Python3 online submissions for Total Cost to Hire K Workers.
    """

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        boundary_left = candidates
        q_left = costs[:boundary_left] + [float('inf')]
        heapq.heapify(q_left)

        boundary_right = n - candidates if n - \
            candidates >= boundary_left else boundary_left
        q_right = costs[boundary_right:] + [float('inf')]
        heapq.heapify(q_right)

        rest = costs[boundary_left:boundary_right]

        cost = 0
        rounds_left = k

        while q_left and q_right and rounds_left:
            rounds_left -= 1
            left = heapq.heappop(q_left)
            right = heapq.heappop(q_right)

            if left <= right:
                cost += left
                heapq.heappush(q_right, right)
                if rest:
                    heapq.heappush(q_left, rest.pop(0))
            else:
                cost += right
                heapq.heappush(q_left, left)
                if rest:
                    heapq.heappush(q_right, rest.pop())

        return cost


class Solution1:
    """
    leetcode solution 1: two priority queues
    Time: O((k+m) * log(m)) -- m = candidates
    Space: O(m)
    Runtime: 793 ms, faster than 77.18% of Python3 online submissions for Total Cost to Hire K Workers.
    Memory Usage: 27 MB, less than 81.88% of Python3 online submissions for Total Cost to Hire K Workers.
    """

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # head_workers stores the first k workers
        # tail_workers stores at most last k workers without any workers from the first k workers
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        answer = 0
        next_head = candidates
        next_tail = len(costs) - 1 - candidates

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heapq.heappop(head_workers)

                # only refill the queue if there are workers outside the two queues
                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heapq.heappop(tail_workers)

                # only refill the queue if there are workers outside the two queues
                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer


class Solution2:
    """
    leetcode solution 2: one priority queue
    Time: O((k+m) * log(m)) -- m = candidates
    Space: O(m)
    Runtime: 920 ms, faster than 40.00% of Python3 online submissions for Total Cost to Hire K Workers.
    Memory Usage: 27.9 MB, less than 40.40% of Python3 online submissions for Total Cost to Hire K Workers.
    """

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # add the first k workers with section id of 0 and
        # the last k workers with section id of 1 (without duplication) to pq
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapq.heapify(pq)

        answer = 0
        next_head = candidates
        next_tail = len(costs) - 1 - candidates

        # only refill pq if there are workers outside pq
        for _ in range(k):
            cur_cost, cur_section_id = heapq.heappop(pq)
            answer += cur_cost
            if next_head <= next_tail:
                if cur_section_id == 0:
                    heapq.heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heapq.heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1

        return answer


s = Solution()
tests = [
    (([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4),
     11),

    (([1, 2, 4, 1], 3, 3),
     4),
]
for inp, exp in tests:
    res = s.totalCost(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
