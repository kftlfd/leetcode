"""
Leetcode
823. Binary Trees With Factors (medium)
2023-10-26

Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

 

Constraints:

    1 <= arr.length <= 1000
    2 <= arr[i] <= 10^9
    All the values of arr are unique.
"""

from typing import List


class Solution:
    """
    Runtime: 274 ms, faster than 84.03% of Python3 online submissions for Binary Trees With Factors.
    Memory Usage: 16.4 MB, less than 68.07% of Python3 online submissions for Binary Trees With Factors.
    """

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        A = arr
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0:  # A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD


s = Solution()
tests = [
    ([2, 4],
     3),

    ([2, 4, 5, 10],
        7),
]
for inp, exp in tests:
    res = s.numFactoredBinaryTrees(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
