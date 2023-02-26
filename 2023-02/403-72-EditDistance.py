"""
Leetcode
72. Edit Distance (hard)
2023-02-26

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

from typing import List, Optional


class Solution:
    """
    leetcode solution 1: recursion
    Time Limit Exceeded
    """

    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))

    def minDistanceRecur(self, word1: str, word2: str, idx1: int, idx2: int) -> int:
        if idx1 == 0:
            return idx2

        if idx2 == 0:
            return idx1

        if word1[idx1 - 1] == word2[idx2 - 1]:
            return self.minDistanceRecur(word1, word2, idx1 - 1, idx2 - 1)

        insertOp = self.minDistanceRecur(word1, word2, idx1, idx2 - 1)
        deleteOp = self.minDistanceRecur(word1, word2, idx1 - 1, idx2)
        replceOp = self.minDistanceRecur(word1, word2, idx1 - 1, idx2 - 1)
        return min(insertOp, deleteOp, replceOp) + 1


class Solution1:
    """
    leetcode solution 2: Memoization: Top-Down Dynamic Programming
    Runtime: 98 ms, faster than 91.64% of Python3 online submissions for Edit Distance.
    Memory Usage: 17.2 MB, less than 71.69% of Python3 online submissions for Edit Distance.
    """
    memo = [[]]

    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = [[None for i in range(len(word2) + 1)]
                     for j in range(len(word1) + 1)]
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))

    def minDistanceRecur(self, word1: str, word2: str, idx1: int, idx2: int) -> int:
        if idx1 == 0:
            return idx2

        if idx2 == 0:
            return idx1

        if self.memo[idx1][idx2]:
            return self.memo[idx1][idx2]

        min_edit_distance = 0

        if word1[idx1 - 1] == word2[idx2 - 1]:
            min_edit_distance = self.minDistanceRecur(
                word1, word2, idx1 - 1, idx2 - 1)

        else:
            insertOp = self.minDistanceRecur(word1, word2, idx1, idx2 - 1)
            deleteOp = self.minDistanceRecur(word1, word2, idx1 - 1, idx2)
            replceOp = self.minDistanceRecur(word1, word2, idx1 - 1, idx2 - 1)
            min_edit_distance = min(insertOp, deleteOp, replceOp) + 1

        self.memo[idx1][idx2] = min_edit_distance
        return min_edit_distance


class Solution2:
    """
    leetcode solution 3: Bottom-Up Dynamic Programming: Tabulation
    Runtime: 157 ms, faster than 74.49% of Python3 online submissions for Edit Distance.
    Memory Usage: 17.7 MB, less than 29.79% of Python3 online submissions for Edit Distance.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1

        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for idx1 in range(1, l1 + 1):
            dp[idx1][0] = idx1

        for idx2 in range(1, l2 + 1):
            dp[0][idx2] = idx2

        for idx1 in range(1, l1 + 1):
            for idx2 in range(1, l2 + 1):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1]
                else:
                    dp[idx1][idx2] = min(
                        dp[idx1 - 1][idx2 - 1],
                        dp[idx1 - 1][idx2],
                        dp[idx1][idx2 - 1]
                    ) + 1

        return dp[l1][l2]


s = Solution2()
tests = [
    (("park", "spake"),
     3),

    (("horse", "ros"),
     3),

    (("intention", "execution"),
     5),
]
for inp, exp in tests:
    res = s.minDistance(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
