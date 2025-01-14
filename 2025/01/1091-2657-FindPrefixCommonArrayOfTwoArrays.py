"""
Leetcode
2025-01-14
2657. Find the Prefix Common Array of Two Arrays
Medium

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

 

Constraints:

    1 <= A.length == B.length == n <= 50
    1 <= A[i], B[i] <= n
    It is guaranteed that A and B are both a permutation of n integers.

Hint 1
Consider keeping a frequency array that stores the count of occurrences of each number till index i.
Hint 2
If a number occurred two times, it means it occurred in both A and B since they’re both permutations so add one to the answer.
"""

from typing import List


class Solution00:
    """
    Runtime 17ms Beats 41.41%
    Memory 17.80MB Beats 32.03%
    """

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        set_a = set()
        set_b = set()
        ans = [0] * n

        for i in range(n):
            set_a.add(A[i])
            set_b.add(B[i])
            ans[i] = len(set_a.intersection(set_b))

        return ans


class Solution01:
    """
    Runtime 7ms Beats 75.00%
    Memory 17.82MB Beats 19.53%
    """

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        ans = [0] * n
        cur = 0

        for i, (a, b) in enumerate(zip(A, B)):
            freq[a] += 1
            freq[b] += 1
            if a == b:
                cur += 1
            else:
                cur += freq[a] == 2
                cur += freq[b] == 2
            ans[i] = cur

        return ans
