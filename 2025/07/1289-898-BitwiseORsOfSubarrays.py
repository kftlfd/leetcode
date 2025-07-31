"""
Leetcode
2025-07-31
898. Bitwise ORs of Subarrays
Medium

Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.

Example 2:

Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.

Example 3:

Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.

 

Constraints:

    1 <= arr.length <= 5 * 10^4
    0 <= arr[i] <= 10^9


"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        ors = set()

        def dfs(i: int, cur_or: int):
            if i >= n:
                return
            num = arr[i]
            with_num = cur_or | num
            ors.add(num)
            dfs(i + 1, num)
            ors.add(with_num)
            dfs(i + 1, with_num)

        dfs(0, 0)
        return len(ors)


class Solution1:
    """
    leetcode solution: Frontier Set
    Runtime 477ms Beats 23.22%
    Memory 44.86MB Beats 51.19%
    """

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
