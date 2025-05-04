"""
Leetcode
2025-05-04
1128. Number of Equivalent Domino Pairs
Easy

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3

 

Constraints:

    1 <= dominoes.length <= 4 * 10^4
    dominoes[i].length == 2
    1 <= dominoes[i][j] <= 9


Hint 1
For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.
Hint 2
You can keep track of what you've seen using a hashmap.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime 9ms Beats 77.32%
    Memory 24.30MB Beats 81.31%
    """

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter()
        ans = 0

        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            ans += cnt[key]
            cnt[key] += 1

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 7ms Beats 92.01%
    Memory 24.32MB Beats 43.37%
    """

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            ret += num[val]
            num[val] += 1
        return ret
