"""
Leetcode
2026-05-20
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


"""

from typing import List


class Solution:
    """
    Runtime 4ms Beats 79.26%
    Memory 19.32MB Beats 34.04%
    """

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        common = 0
        ans = [0] * n

        for i, (a, b) in enumerate(zip(A, B)):
            if a == b:
                common += 1
            else:
                freq[a] += 1
                freq[b] += 1
                common += (freq[a] % 2 == 0) + (freq[b] % 2 == 0)
            ans[i] = common

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 0ms Beats 100.00%
    Memory 19.22MB Beats 73.05%
    """

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        frequency = [0 for _ in range(n + 1)]
        common_count = 0

        # Iterate through the elements of both arrays
        for current_index in range(n):

            # Increment frequency of current elements in A and B
            # Check if the element in A has appeared before (common in prefix)
            frequency[A[current_index]] += 1
            if frequency[A[current_index]] == 2:
                common_count += 1

            # Check if the element in B has appeared before (common in prefix)
            frequency[B[current_index]] += 1
            if frequency[B[current_index]] == 2:
                common_count += 1

            # Store the count of common elements for the current prefix
            prefix_common_array[current_index] = common_count

        # Return the final array with counts of common elements in each prefix
        return prefix_common_array
