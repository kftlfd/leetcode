"""
Leetcode
1354. Construct Target Array With Multiple Sums (hard)
2022-06-24

You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

 - let x be the sum of all elements currently in your array.
 - choose index i, such that 0 <= i < n and set the value of arr at index i to x.
 - You may repeat this procedure as many times as needed.

Return true if it is possible to construct the target array from arr, otherwise, return false.

Example 1:
Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:
Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
"""

from typing import List
import heapq


# https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC++Python-Backtrack-OJ-is-wrong
# Runtime: 405 ms, faster than 54.12% of Python3 online submissions for Construct Target Array With Multiple Sums.
# Memory Usage: 20 MB, less than 55.29% of Python3 online submissions for Construct Target Array With Multiple Sums.
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-a for a in target]
        heapq.heapify(target)
        while True:
            a = -heapq.heappop(target)
            total -= a
            if a == 1 or total == 1:
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(target, -a)


s = Solution()
tests = [
    [9, 3, 5],
    [1, 1, 1, 2],
    [8, 5],
]
for t in tests:
    print(t)
    print()
    print()
