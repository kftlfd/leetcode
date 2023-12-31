"""
Leetcode
2244. Minimum Rounds to Complete All Tasks (medium)
2023-01-04

You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

Example 1:
Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

Example 2:
Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
"""

from typing import List, Optional
from collections import Counter


# Runtime: 1864 ms, faster than 47.22% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
# Memory Usage: 28.3 MB, less than 70.66% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        task_cnt = Counter(tasks)
        rounds = 0

        for n in task_cnt.values():
            # can do tasks only in batches of 2 or 3
            if n == 1:
                return -1
            # divide number of tasks in rounds of 3
            # if remainder is 0 -> no extra rounds needed (+0)
            # if remainder is 1 -> remove one round of 3 (now 4 tasks left) and add two rounds of 2, so +1 extra round
            # if remainder is 2 -> +1 extra round of 2
            rounds += (n // 3) + (n % 3 != 0)

        return rounds


s = Solution()
tests = [
    ([2, 2, 3, 3, 2, 4, 4, 4, 4, 4],
     4),

    ([2, 3, 3],
     -1)
]
for inp, exp in tests:
    res = s.minimumRounds(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
