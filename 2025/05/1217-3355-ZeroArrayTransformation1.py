"""
Leetcode
2025-05-20
3355. Zero Array Transformation I
Medium

You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

    Select a 

    of indices within the range [li, ri] in nums.
    Decrement the values at the selected indices by 1.

A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

 

Example 1:

Input: nums = [1,0,1], queries = [[0,2]]

Output: true

Explanation:

    For i = 0:
        Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
        The array will become [0, 0, 0], which is a Zero Array.

Example 2:

Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]

Output: false

Explanation:

    For i = 0:
        Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
        The array will become [4, 2, 1, 0].
    For i = 1:
        Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
        The array will become [3, 1, 0, 0], which is not a Zero Array.

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
    1 <= queries.length <= 10^5
    queries[i].length == 2
    0 <= li <= ri < nums.length


Hint 1
Can we use difference array and prefix sum to check if an index can be made zero?
"""

from typing import List


class Solution:
    """
    Runtime 71ms Beats 83.30%
    Memory 55.07MB Beats 52.93%
    """

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        cur = 0
        for i, num in enumerate(nums):
            cur += diff[i]
            if num > cur:
                return False

        return True


class Solution1:
    """
    leetcode solution: Difference Array
    Runtime 83ms Beats 57.92%
    Memory 55.76MB Beats 20.15%
    """

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            currentOperations += delta
            operationCounts.append(currentOperations)
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True
