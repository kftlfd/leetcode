"""
Leetcode
1964. Find the Longest Valid Obstacle Course at Each Position (hard)
2023-05-07

You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

    You choose any number of obstacles between 0 and i inclusive.
    You must include the ith obstacle in the course.
    You must put the chosen obstacles in the same order as they appear in obstacles.
    Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.

Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.

Example 1:
Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.

Example 2:
Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [2,2,1], [1] has length 1.

Example 3:
Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [3,1], [1] has length 1.
- i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
- i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,1,5,6,4,2], [1,2] has length 2.
"""

from typing import List
from bisect import bisect_right


class Solution:
    """
    leetcode solution 1: greedy + binary search
    Runtime: 1483 ms, faster than 98.48% of Python3 online submissions for Find the Longest Valid Obstacle Course at Each Position.
    Memory Usage: 34.1 MB, less than 15.15% of Python3 online submissions for Find the Longest Valid Obstacle Course at Each Position.
    """

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1] * n

        # lis[i] records the lowest increasing sequence of length i + 1
        lis = []

        for i, height in enumerate(obstacles):
            # Find the rightmost insertion position idx.
            idx = bisect_right(lis, height)

            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            ans[i] = idx + 1

        return ans


s = Solution()
tests = [
    ([1, 2, 3, 2],
     [1, 2, 3, 3]),

    ([2, 2, 1],
     [1, 2, 1]),

    ([3, 1, 5, 6, 4, 2],
     [1, 1, 2, 3, 2, 2]),
]
for inp, exp in tests:
    res = s.longestObstacleCourseAtEachPosition(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
