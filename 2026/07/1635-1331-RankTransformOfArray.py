"""
Leetcode
2026-07-12
1331. Rank Transform of an Array
Easy

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.

 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]

 

Constraints:

    0 <= arr.length <= 10^5
    -10^9 <= arr[i] <= 10^9


"""

from typing import List


class Solution01:
    """
    Runtime 43ms Beats 49.91%
    Memory 37.66MB Beats 39.04%
    """

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        nxt_rank = 1

        for num in sorted(arr):
            if num not in rank:
                rank[num] = nxt_rank
                nxt_rank += 1

        return [rank[num] for num in arr]


class Solution02:
    """
    Runtime 31ms Beats 93.30%
    Memory 37.56MB Beats 60.61%
    """

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        nxt_rank = 1

        for num in sorted(set(arr)):
            rank[num] = nxt_rank
            nxt_rank += 1

        return [rank[num] for num in arr]


class Solution3:
    """
    leetcode solution 3: Ordered Map
    Runtime 85ms Beats 8.52%
    Memory 49.97MB Beats 5.04%
    """

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Store the rank for each number in arr
        num_to_indices = {k: [] for k in sorted(set(arr))}

        for i, num in enumerate(arr):
            num_to_indices[num].append(i)

        rank = 1
        for num in num_to_indices.keys():
            for index in num_to_indices[num]:
                arr[index] = rank
            rank += 1

        return arr
