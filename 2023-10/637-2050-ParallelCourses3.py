"""
Leetcode
2050. Parallel Courses III (hard)
2023-10-18

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:

    You may start taking a course at any time if the prerequisites are met.
    Any number of courses can be taken at the same time.

Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

 

Example 1:

Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
Output: 8
Explanation: The figure above represents the given graph and the time required to complete each course. 
We start course 1 and course 2 simultaneously at month 0.
Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.

Example 2:

Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
Output: 12
Explanation: The figure above represents the given graph and the time required to complete each course.
You can start courses 1, 2, and 3 at month 0.
You can complete them after 1, 2, and 3 months respectively.
Course 4 can be taken only after course 3 is completed, i.e., after 3 months. It is completed after 3 + 4 = 7 months.
Course 5 can be taken only after courses 1, 2, 3, and 4 have been completed, i.e., after max(1,2,3,7) = 7 months.
Thus, the minimum time needed to complete all the courses is 7 + 5 = 12 months.

 

Constraints:

    1 <= n <= 5 * 10^4
    0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)
    relations[j].length == 2
    1 <= prevCoursej, nextCoursej <= n
    prevCoursej != nextCoursej
    All the pairs [prevCoursej, nextCoursej] are unique.
    time.length == n
    1 <= time[i] <= 10^4
    The given graph is a directed acyclic graph.
"""

from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    """
    Wrong answer
    """

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        def t(course: int) -> int:
            return time[course - 1]

        prev_courses = defaultdict(list)
        next_courses = defaultdict(list)

        for prev, course in relations:
            prev_courses[course].append(prev)
            next_courses[prev].append(course)

        roots = []
        for course in range(1, n + 1):
            if not next_courses[course]:
                roots.append(course)

        time_needed = 0

        for root in roots:
            q = [root]
            curr_root_time = 0
            while q:
                nxt_q = []
                curr_row_time = 0
                for course in q:
                    curr_row_time = max(curr_row_time, t(course))
                    nxt_q += prev_courses[course]
                curr_root_time += curr_row_time
                q = nxt_q
            time_needed = max(time_needed, curr_root_time)

        return time_needed


class Solution1:
    """
    leetcode solution 1: topological sort, Kahn's algorithm
    Time: O(n + len(relations))
    Space: O(n + len(relations))
    Runtime: 1407 ms, faster than 83.24% of Python3 online submissions for Parallel Courses III.
    Memory Usage: 45.2 MB, less than 89.71% of Python3 online submissions for Parallel Courses III.
    """

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        indegree = [0] * n

        for (x, y) in relations:
            graph[x - 1].append(y - 1)
            indegree[y - 1] += 1

        q = deque()
        max_time = [0] * n
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                max_time[node] = time[node]

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                max_time[neighbor] = max(
                    max_time[neighbor], max_time[node] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return max(max_time)


class Solution2:
    """
    leetcode solution 2: dfs + memoization (top-down dp)
    Time: O(n + len(relations))
    Space: O(n + len(relations))
    Runtime: 1425 ms, faster than 73.24% of Python3 online submissions for Parallel Courses III.
    Memory Usage: 95 MB, less than 10.59% of Python3 online submissions for Parallel Courses III.
    """

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)

        for (x, y) in relations:
            graph[x - 1].append(y - 1)

        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]

            ans = 0
            for neighbor in graph[node]:
                ans = max(ans, dfs(neighbor))

            return time[node] + ans

        ans = 0
        for node in range(n):
            ans = max(ans, dfs(node))

        return ans


s = Solution()
tests = [
    ((3, [[1, 3], [2, 3]], [3, 2, 5]),
     8),

    ((5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]),
     12),

    ((9,
      [[2, 7], [2, 6], [3, 6], [4, 6], [7, 6], [2, 1], [3, 1], [4, 1], [6, 1],
          [7, 1], [3, 8], [5, 8], [7, 8], [1, 9], [2, 9], [6, 9], [7, 9]],
        [9, 5, 9, 5, 8, 7, 7, 8, 4]),
        32),
]
for inp, exp in tests:
    res = s.minimumTime(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
