"""
Leetcode
2025-07-26
3480. Maximize Subarrays After Removing One Conflicting Pair
Hard

You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. Afterward, count the number of

of nums which do not contain both a and b for any remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.

 

Example 1:

Input: n = 4, conflictingPairs = [[2,3],[1,4]]

Output: 9

Explanation:

    Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
    There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.

Example 2:

Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]

Output: 12

Explanation:

    Remove [1, 2] from conflictingPairs. Now, conflictingPairs = [[2, 5], [3, 5]].
    There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together.
    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 12.

 

Constraints:

    2 <= n <= 10^5
    1 <= conflictingPairs.length <= 2 * n
    conflictingPairs[i].length == 2
    1 <= conflictingPairs[i][j] <= n
    conflictingPairs[i][0] != conflictingPairs[i][1]

    
Hint 1
Let f[i] (where i = 1, 2, 3, ..., n) be the end index of the longest valid subarray (without any conflicting pair) starting at index i.
Hint 2
The answer is: sigma(f[i] - i + 1) for i in [1..n], which simplifies to: sigma(f[i]) - n * (n + 1) / 2 + n.
Hint 3
Focus on maintaining f[i].
Hint 4
If we have a conflicting pair (x, y) with x < y: 1. Sort the conflicting pairs by y values in non-increasing order. 2. Update each prefix of the f array accordingly.
Hint 5
Use a segment tree or another suitable data structure to maintain the range update and sum query efficiently.
"""

from typing import List


class Solution1:
    """
    leetcode solution: Enumeration
    Runtime 979ms Beats 45.05%
    Memory 85.16MB Beats 99.10%
    """

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        bMin1 = [2**31 - 1] * (n + 1)
        bMin2 = [2**31 - 1] * (n + 1)
        for pair in conflictingPairs:
            a = min(pair[0], pair[1])
            b = max(pair[0], pair[1])
            if bMin1[a] > b:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif bMin2[a] > b:
                bMin2[a] = b
        res = 0
        ib1 = n
        b2 = 0x3FFFFFFF
        delCount = [0] * (n + 1)
        for i in range(n, 0, -1):
            if bMin1[ib1] > bMin1[i]:
                b2 = min(b2, bMin1[ib1])
                ib1 = i
            else:
                b2 = min(b2, bMin1[i])
            res += min(bMin1[ib1], n + 1) - i
            delCount[ib1] += min(b2, bMin2[ib1], n + 1) - min(
                bMin1[ib1], n + 1
            )
        return res + max(delCount)
