"""
Leetcode
630. Course Schedule III (hard)
2022-06-23

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.
"""

from typing import List
import heapq



# https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
# Runtime: 1530 ms, faster than 9.16% of Python3 online submissions for Course Schedule III.
# Memory Usage: 19.3 MB, less than 97.25% of Python3 online submissions for Course Schedule III.
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        start = 0
        for t,end in sorted(courses, key=lambda x: x[1]):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)



s = Solution()
tests = [
    [[100,200],[200,1300],[1000,1250],[2000,3200]],
    [[1,2]],
    [[3,2],[4,3]],
]
for t in tests:
    print(t)
    print(s.scheduleCourse(t))
    print()
