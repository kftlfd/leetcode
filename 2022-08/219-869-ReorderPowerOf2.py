"""
Leetcode
869. Reordered Power of 2 (medium)
2022-08-26

You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 10
Output: false
"""

import itertools
import collections


# leetcode solution - Approach 1: Permutations
# Runtime: 4184 ms, faster than 15.51% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 13.9 MB, less than 26.74% of Python3 online submissions for Reordered Power of 2.
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Let's work through an example like N = 128.
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.
        """
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(n)))


# leetcode solution - Approach 2: Counting
# Runtime: 79 ms, faster than 31.55% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 13.9 MB, less than 64.17% of Python3 online submissions for Reordered Power of 2.
class Solution1:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))


s = Solution()
tests = [
    1, 10
]
for t in tests:
    print(t)
    print(s.reorderedPowerOf2(t))
    print()
