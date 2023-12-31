"""
Leetcode
338. Counting Bits (easy)
2023-09-01

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:

    0 <= n <= 10^5
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/counting-bits/discuss/79557/How-we-handle-this-question-on-interview-Thinking-process-+-DP-solution
    Runtime: 60 ms, faster than 97.97% of Python3 online submissions for Counting Bits.
    Memory Usage: 23 MB, less than 94.90% of Python3 online submissions for Counting Bits.
    """

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            ans[i] = ans[i - offset] + 1
        return ans


s = Solution()
tests = [
    (2,
     [0, 1, 1]),

    (5,
     [0, 1, 1, 2, 1, 2])
]
for inp, exp in tests:
    res = s.countBits(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
