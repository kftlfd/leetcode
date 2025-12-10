"""
Leetcode
2025-12-10
3577. Count the Number of Computer Unlocking Permutations
Medium

You are given an array complexity of length n.

There are n locked computers in a room with labels from 0 to n - 1, each with its own unique password. The password of the computer i has a complexity complexity[i].

The password for the computer labeled 0 is already decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:

    You can decrypt the password for the computer i using the password for computer j, where j is any integer less than i with a lower complexity. (i.e. j < i and complexity[j] < complexity[i])
    To decrypt the password for computer i, you must have already unlocked a computer j such that j < i and complexity[j] < complexity[i].

Find the number of

of [0, 1, 2, ..., (n - 1)] that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.

Since the answer may be large, return it modulo 109 + 7.

Note that the password for the computer with label 0 is decrypted, and not the computer with the first position in the permutation.

 

Example 1:

Input: complexity = [1,2,3]

Output: 2

Explanation:

The valid permutations are:

    [0, 1, 2]
        Unlock computer 0 first with root password.
        Unlock computer 1 with password of computer 0 since complexity[0] < complexity[1].
        Unlock computer 2 with password of computer 1 since complexity[1] < complexity[2].
    [0, 2, 1]
        Unlock computer 0 first with root password.
        Unlock computer 2 with password of computer 0 since complexity[0] < complexity[2].
        Unlock computer 1 with password of computer 0 since complexity[0] < complexity[1].

Example 2:

Input: complexity = [3,3,3,4,4,4]

Output: 0

Explanation:

There are no possible permutations which can unlock all computers.

 

Constraints:

    2 <= complexity.length <= 10^5
    1 <= complexity[i] <= 10^9

"""

from collections import Counter
from typing import List


class Solution01:
    """
    Runtime 36ms Beats 29.44%
    Memory 38.77MB Beats 11.11%
    """

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        freq = Counter(complexity)
        MOD = 10**9 + 7

        if freq[complexity[0]] != 1 or complexity[0] != min(freq.keys()):
            return 0

        ans = 1
        for i in range(n - 1, 1, -1):
            ans = (ans * i) % MOD

        return ans


class Solution02:
    """
    Runtime 9ms Beats 96.11%
    Memory 31.90MB Beats 82.78%
    """

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        minVal = complexity[0]
        for i in range(1, n):
            if complexity[i] <= minVal:
                return 0

        ans = 1
        MOD = 10**9 + 7
        for i in range(n - 1, 1, -1):
            ans = (ans * i) % MOD

        return ans


class Solution1:
    """
    leetcode solution: Brain Teaser
    Runtime 19ms Beats 65.56%
    Memory 31.94MB Beats 52.78%
    """

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans, mod = 1, 10**9 + 7
        for i in range(2, n):
            ans = ans * i % mod
        return ans
