"""
Leetcode
77. Combinations (medium)
2023-08-01

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:

    1 <= n <= 20
    1 <= k <= n
"""

from typing import List
from itertools import combinations


class Solution:
    """
    Runtime: 502 ms, faster than 11.74% of Python3 online submissions for Combinations.
    Memory Usage: 72.2 MB, less than 7.13% of Python3 online submissions for Combinations.
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        ans = [[x] for x in nums]

        for _ in range(1, k):
            ans2 = []
            for comb in ans:
                i = comb[-1]
                for nxt_num in nums[i:]:
                    ans2.append(comb + [nxt_num])
            ans = ans2

        return ans


class Solution1:
    """
    https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
    Runtime: 505 ms, faster than 11.46% of Python3 online submissions for Combinations.
    Memory Usage: 72.1 MB, less than 7.13% of Python3 online submissions for Combinations.
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [
                [i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs


class Solution2:
    """
    Runtime: 75 ms, faster than 99.37% of Python3 online submissions for Combinations.
    Memory Usage: 18.3 MB, less than 34.56% of Python3 online submissions for Combinations.
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))


s = Solution()
tests = [
    ((4, 2),
     [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),

    ((1, 1),
     [[1]]),
]
for inp, exp in tests:
    res = s.combine(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
