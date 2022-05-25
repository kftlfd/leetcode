"""
Leetcode
354. Russian Doll Envelopes (hard)
2022-05-25

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.
"""

from typing import List



# https://leetcode.com/problems/russian-doll-envelopes/discuss/1134011/JS-Python-Java-C++-or-Easy-LIS-Solution-w-Explanation
# Runtime: 2261 ms, faster than 15.70% of Python3 online submissions for Russian Doll Envelopes.
# Memory Usage: 61.6 MB, less than 67.23% of Python3 online submissions for Russian Doll Envelopes.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        dp = []
        for _,height in env:
            left = bisect_left(dp, height)
            if left == len(dp): dp.append(height)
            else: dp[left] = height
        return len(dp)



s = Solution()
tests = [
    [[5,4],[6,4],[6,7],[2,3]],
    [[1,1],[1,1],[1,1]]
]
for t in tests:
    print(t)
    print(s.maxEnvelopes(t))
    print()
