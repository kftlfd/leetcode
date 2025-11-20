"""
Leetcode
2025-11-20
757. Set Intersection Size At Least Two
Hard

You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

    For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.

Return the minimum possible size of a containing set.

 

Example 1:

Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.

Example 2:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.

Example 3:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.

 

Constraints:

    1 <= intervals.length <= 3000
    intervals[i].length == 2
    0 <= starti < endi <= 10^8


"""

from typing import List


class Solution:
    """
    Wrong Answer
    """

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        cset = []

        for start, end in sorted(intervals):
            if not cset:
                cset.append(end - 1)
                cset.append(end)
                continue
            add = (cset[-2] < start) + (cset[-1] < start)
            if add == 1:
                cset.append(end)
            elif add == 2:
                cset.append(end - 1)
                cset.append(end)

        return len(cset)


class Solution1:
    """
    leetcode solution 1: Greedy
    Runtime 547ms Beats 5.52%
    Memory 19.26MB Beats 17.24%
    """

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in range(s, s + t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans
