"""
Leetcode
2026-01-26
1200. Minimum Absolute Difference
Easy

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr

 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

 

Constraints:

    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6


"""

from typing import List


class Solution:
    """
    Runtime 46ms Beats 81.46%
    Memory 31.38MB Beats38.49%
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        min_diff = 9999999
        ans = []

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            diff = b - a
            if diff < min_diff:
                min_diff = diff
                ans = [[a, b]]
            elif diff == min_diff:
                ans.append([a, b])

        return ans
