"""
Leetcode
1376. Time Needed to Inform All Employees (medium)
2023-06-03

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

Constraints:

    1 <= n <= 105
    0 <= headID < n
    manager.length == n
    0 <= manager[i] < n
    manager[headID] == -1
    informTime.length == n
    0 <= informTime[i] <= 1000
    informTime[i] == 0 if employee i has no subordinates.
    It is guaranteed that all the employees can be informed.
"""

from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = defaultdict(list)

        for i, m in enumerate(manager):
            if m != -1:
                graph[m].append(i)

        q = [(headID, informTime[headID])]

        max_time = 0

        while q:
            employee, cur_time = q.pop(0)

            max_time = max(max_time, cur_time)

            for next_employee in graph[employee]:
                q.append((next_employee, cur_time + informTime[next_employee]))

        return max_time


class Solution1:
    """
    https://leetcode.com/problems/time-needed-to-inform-all-employees/solution/1914698
    Runtime: 1141 ms, faster than 94.35% of Python3 online submissions for Time Needed to Inform All Employees.
    Memory Usage: 89 MB, less than 5.04% of Python3 online submissions for Time Needed to Inform All Employees.
    """

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        @cache
        def get_notification_time(i):
            if (manager_id := manager[i]) != -1:
                return informTime[manager_id] + get_notification_time(manager_id)
            else:
                return 0

        return max(get_notification_time(i) for i in range(n))


s = Solution1()
tests = [
    ((1, 0, [-1], [0]),
     0),

    ((6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]),
     1),
]
for inp, exp in tests:
    res = s.numOfMinutes(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
