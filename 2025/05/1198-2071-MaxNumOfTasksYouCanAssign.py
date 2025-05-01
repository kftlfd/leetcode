"""
Leetcode
2025-05-01
2071. Maximum Number of Tasks You Can Assign
Hard

You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.



Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.



Constraints:

    n == tasks.length
    m == workers.length
    1 <= n, m <= 5 * 10^4
    0 <= pills <= m
    0 <= tasks[i], workers[j], strength <= 10^9


Hint 1
Is it possible to assign the first k smallest tasks to the workers?
Hint 2
How can you efficiently try every k?
"""

from collections import deque
from typing import List
from sortedcontainers import SortedList


class Solution:
    """
    Wrong Answer
    """

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(workers)
        workers = sorted(workers)
        tasks = sorted(tasks)[:n]

        def is_possible(n_tasks: int) -> bool:
            pills_left = pills
            for i in range(n_tasks):
                w = workers[n - 1 - i]
                t = tasks[n_tasks - 1 - i]
                if w >= t:
                    continue
                if pills_left > 0 and w + strength >= t:
                    pills_left -= 1
                    continue
                return False
            return True

        ans = 0
        left = 0
        right = n + 1
        while left < right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid

        return ans


class Solution1:
    """
    leetcode solution: Binary Search + Greedy Selection of Workers
    Runtime 1654ms Beats 16.61%
    Memory 26.80MB Beats 11.28%
    """

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks = sorted(tasks)
        workers = sorted(workers)

        def check(mid: int) -> bool:
            p = pills
            # Ordered set of workers
            ws = SortedList(workers[m - mid:])
            # Enumerate each task from largest to smallest
            for i in range(mid - 1, -1, -1):
                # If the largest element in the ordered set is greater than or equal to tasks[i]
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


class Solution2:
    """
    sample 436ms solution
    Runtime 443ms Beats 86.52%
    Memory 26.17MB Beats 58.93%
    """

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks = sorted(tasks)
        workers = sorted(workers)

        def can_finish(mid, pills):
            n = len(workers)
            i = 0

            # record the mid valid tasks
            queue = deque()

            for j in range(n - mid, n):
                w = workers[j]
                # put m tasks into the queue
                while i < mid and tasks[i] <= w + strength:
                    queue.append(tasks[i])
                    i += 1
                # Now we have found the eligible at most m tasks that workers[j] can finish
                # and have put these tasks into the queue

                # below are to find the most smallest strength task that workers[j] can finish

                # First check, if no tasks were added, this means workers[j] can finish nothing
                if not queue:
                    return False

                # Case 1: if workers[j] can finish task queue[0] without eating pills,
                # then this is what we want, that is, the powerful worker finish the smallest task.
                if queue[0] <= w:
                    queue.popleft()

                # Case 2: if workers[j] needs to eat pills to finish
                # Once he needs to eat pill, we choose the hardest task for him
                # since the left tasks for the others workers will be easy to finish.
                else:
                    # need to eat pills
                    if pills == 0:
                        return False

                    pills -= 1
                    queue.pop()

                # after this loop, it means for the workers[j],
                # he can finish the one task that is <= his strength + strength of pills
            return True

        # standard Binary Search
        left = 0
        right = min(len(tasks), len(workers))
        while left < right:
            mid = (left + right+1) // 2
            # this guessing mid number is eligible,
            # we can guess larger since we need maximum tasks number
            if can_finish(mid, pills):
                left = mid
            else:
                right = mid - 1

        return left


s = Solution()
tests = [
    (([5, 9, 8, 5, 9], [1, 6, 4, 2, 6], 1, 5),
     3),
]
for inp, exp in tests:
    res = s.maxTaskAssign(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
