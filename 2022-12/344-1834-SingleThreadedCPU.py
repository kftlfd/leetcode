"""
Leetcode
1834. Single-Threaded CPU (medium)
2022-12-29

You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the ith task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

    If the CPU is idle and there are no available tasks to process, the CPU remains idle.
    If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
    Once a task is started, the CPU will process the entire task without stopping.
    The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

Example 1:
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

Example 2:
Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
"""

from typing import List, Optional
import heapq
from math import inf


# Time Limit Exceeded
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        clock = 1
        tasks_order = []

        while len(tasks_order) < len(tasks):
            available_tasks = [i for i, t in enumerate(tasks) if (
                (t[0] <= clock) and (i not in tasks_order))]

            if not available_tasks:
                clock += 1
                continue

            curr_task = available_tasks[-1]
            for t in available_tasks[-2::-1]:
                if tasks[t][1] <= tasks[curr_task][1]:
                    curr_task = t

            tasks_order.append(curr_task)
            clock += tasks[curr_task][1]

        return tasks_order


# Wrong Answer
class Solution1:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        clock = 1
        tasks_order = []
        q = []
        for i, t in enumerate(tasks):
            heapq.heappush(q, (t[0], t[1], i))

        while q:
            clock = max(clock, q[0][0])
            q_idx = 0
            t_time = inf
            for i in range(len(q)):
                if q[i][0] > clock:
                    break
                if q[i][1] < t_time:
                    t_time = q[i][1]
                    q_idx = i
            _, task_time, task_index = q.pop(q_idx)
            clock += task_time
            tasks_order.append(task_index)

        return tasks_order


# leetcode solution
# Runtime: 2019 ms, faster than 90.00% of Python3 online submissions for Single-Threaded CPU.
# Memory Usage: 63.5 MB, less than 13.28% of Python3 online submissions for Single-Threaded CPU.
class Solution2:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # Sort based on min task processing time or min task index.
        next_task: List[Tuple[int, int]] = []
        tasks_processing_order: List[int] = []

        # Store task enqueue time, processing time, index.
        sorted_tasks = [(enqueue, process, idx)
                        for idx, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()

        curr_time = 0
        task_index = 0

        # Stop when no tasks are left in array and heap.
        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                # When the heap is empty, try updating curr_time to next task's enqueue time.
                curr_time = sorted_tasks[task_index][0]

            # Push all the tasks whose enqueueTime <= currtTime into the heap.
            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                _, process_time, original_index = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, original_index))
                task_index += 1

            process_time, index = heapq.heappop(next_task)

            # Complete this task and increment curr_time.
            curr_time += process_time
            tasks_processing_order.append(index)

        return tasks_processing_order


s = Solution2()
tests = [
    ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]],
     [4, 3, 2, 0, 1]),

    ([[1, 2], [2, 4], [3, 2], [4, 1]],
     [0, 2, 3, 1]),
]
for inp, exp in tests:
    res = s.getOrder(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
