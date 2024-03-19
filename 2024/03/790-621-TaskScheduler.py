"""
Leetcode
621. Task Scheduler
Medium
2024-03-19

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

    1 <= tasks.length <= 10^4
    tasks[i] is an uppercase English letter.
    0 <= n <= 100
"""

from typing import List
import heapq


class Solution1:
    """
    leetcode solution 1: Using Priority Queue / Max Heap
    Runtime: 419 ms, faster than 66.62% of Python3 online submissions for Task Scheduler.
    Memory Usage: 17.1 MB, less than 79.06% of Python3 online submissions for Task Scheduler.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build frequency map
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1

        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            # Execute tasks in each cycle
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            # Add time for the completed cycle
            time += task_count if not pq else n + 1
        return time


class Solution2:
    """
    leetcode solution 2: Filling the Slots and Sorting
    Runtime: 358 ms, faster than 83.34% of Python3 online submissions for Task Scheduler.
    Memory Usage: 17.1 MB, less than 79.06% of Python3 online submissions for Task Scheduler.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a frequency array to keep track of the count of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Sort the frequency array in non-decreasing order
        freq.sort()
        # Calculate the maximum frequency of any task
        max_freq = freq[25] - 1
        # Calculate the number of idle slots that will be required
        idle_slots = max_freq * n
        # Iterate over the frequency array from the second highest frequency to the lowest frequency

        for i in range(24, -1, -1):
            # Subtract the minimum of the maximum frequency and the current frequency from the idle slots
            idle_slots -= min(max_freq, freq[i])

        # If there are any idle slots left, add them to the total number of tasks
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)


class Solution3:
    """
    leetcode solution 3: Greedy
    Runtime: 383 ms, faster than 74.43% of Python3 online submissions for Task Scheduler.
    Memory Usage: 17.2 MB, less than 24.92% of Python3 online submissions for Task Scheduler.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Counter array to store the frequency of each task
        counter = [0] * 26
        max_val = 0
        max_count = 0

        # Traverse through tasks to calculate task frequencies
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
            if max_val == counter[ord(task) - ord('A')]:
                max_count += 1
            elif max_val < counter[ord(task) - ord('A')]:
                max_val = counter[ord(task) - ord('A')]
                max_count = 1

        # Calculate idle slots, available tasks, and idles needed
        part_count = max_val - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_val * max_count
        idles = max(0, empty_slots - available_tasks)

        # Return the total time required
        return len(tasks) + idles


class Solution4:
    """
    leetcode solution 4: Using Math
    Runtime: 381 ms, faster than 74.68% of Python3 online submissions for Task Scheduler.
    Memory Usage: 17.1 MB, less than 59.31% of Python3 online submissions for Task Scheduler.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq array to store the frequency of each task
        freq = [0] * 26
        max_count = 0

        # Count the frequency of each task and find the maximum frequency
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            max_count = max(max_count, freq[ord(task) - ord('A')])

        # Calculate the total time needed for execution
        time = (max_count - 1) * (n + 1)
        for f in freq:
            if f == max_count:
                time += 1

        # Return the maximum of total time needed and the length of the task list
        return max(len(tasks), time)
