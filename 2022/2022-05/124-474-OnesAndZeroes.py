"""
Leetcode
474. Ones and Zeroes (medium)
2022-05-23

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""

from typing import List



# https://leetcode.com/problems/ones-and-zeroes/discuss/1138534/Python-short-dp-explained
# Runtime: 2742 ms, faster than 88.40% of Python3 online submissions for Ones and Zeroes.
# Memory Usage: 199.6 MB, less than 16.90% of Python3 online submissions for Ones and Zeroes.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        
        def dp(mm, nn, kk):
            if mm < 0 or nn < 0: return -float("inf")
            if kk == len(strs): return 0
            x, y = xy[kk]
            return max(1 + dp(mm-x, nn-y, kk + 1), dp(mm, nn, kk + 1))
        
        return dp(m, n, 0)



s = Solution()
tests = [
    [["10","0001","111001","1","0"], 5, 3],
    [["10","0","1"], 1, 1]
]
for t in tests:
    print(t)
    print(s.findMaxForm(t[0], t[1], y[2]))
    print()
