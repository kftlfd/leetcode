"""
Leetcode
624. Maximum Distance in Arrays
Medium
2024-08-16

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:

Input: arrays = [[1],[1]]
Output: 0

 

Constraints:

    m == arrays.length
    2 <= m <= 105
    1 <= arrays[i].length <= 500
    -104 <= arrays[i][j] <= 104
    arrays[i] is sorted in ascending order.
    There will be at most 105 integers in all the arrays.
"""

from typing import List


class Solution1:
    """
    Wrong Answer
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[1][-1]
        if arrays[0][-1] - arrays[1][0] > cur_max - cur_min:
            cur_min = arrays[1][0]
            cur_max = arrays[0][-1]

        ans = cur_max - cur_min

        for arr in arrays[2:]:
            arr_min, arr_max = arr[0], arr[-1]
            if arr_max > cur_max:
                cur_max = arr_max
            elif arr_min < cur_min:
                cur_min = arr_min
            ans = cur_max - cur_min

        return ans


class Solution2:
    """
    Wrong Answer
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]

        ans = cur_max - cur_min

        for arr in arrays:
            arr_min, arr_max = arr[0], arr[-1]
            choose_min = cur_max - arr_min
            choose_max = arr_max - cur_min
            if choose_min > ans and choose_min > choose_max:
                cur_min = arr_min
            elif choose_max > ans and choose_max > choose_min:
                cur_max = arr_max
            ans = cur_max - cur_min

        return ans


class Solution3:
    """
    Wrong Answer
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]

        ans = -1

        for arr in arrays:
            arr_min, arr_max = arr[0], arr[-1]
            choose_min = cur_max - arr_min
            choose_max = arr_max - cur_min
            if choose_min > choose_max and choose_min > ans:
                cur_min = arr_min
            elif choose_max > ans:
                cur_max = arr_max
            ans = cur_max - cur_min

        return ans


class Solution4:
    """
    https://leetcode.com/problems/maximum-distance-in-arrays/discuss/104658/Short-Python/118342
    Runtime: 1346 ms, faster than 58.33% of Python3 online submissions for Maximum Distance in Arrays.
    Memory Usage: 41.8 MB, less than 74.71% of Python3 online submissions for Maximum Distance in Arrays.
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        minnum = arrays[0][0]
        maxnum = arrays[0][-1]
        maxdiff = float('-inf')

        for array in arrays[1:]:
            maxdiff = max(maxdiff, array[-1]-minnum, maxnum-array[0])
            minnum = min(minnum, array[0])
            maxnum = max(maxnum, array[-1])

        return maxdiff


s = Solution3()
tests = [
    ([[1, 5], [3, 4]],
     3),
    ([[1, 4], [0, 5]],
     4),
    ([[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]],
     14),
]
for inp, exp in tests:
    res = s.maxDistance(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
