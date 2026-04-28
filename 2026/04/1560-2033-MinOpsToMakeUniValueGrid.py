"""
Leetcode
2026-04-28
2033. Minimum Operations to Make a Uni-Value Grid
Medium

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:

Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:

Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:

Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10^5
    1 <= m * n <= 10^5
    1 <= x, grid[i][j] <= 10^4

Hint 1
Is it possible to make two integers a and b equal if they have different remainders dividing by x?
Hint 2
If it is possible, which number should you select to minimize the number of operations?
"""

from typing import List


class Solution:
    """
    Runtime 175ms Beats 40.41%
    Memory 40.58MB Beats 99.32%
    """

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(num for row in grid for num in row)

        if x != 1:
            rem = nums[0] % x
            if not all(num % x == rem for num in nums):
                return -1

        if len(nums) % 2 == 1:
            mid = len(nums) // 2
            target = nums[mid]
            return sum(abs(target - num) // x for num in nums)

        mid = len(nums) // 2
        target1 = nums[mid]
        ans1 = sum(abs(target1 - num) // x for num in nums)

        if nums[mid - 1] == target1:
            return ans1

        target2 = nums[mid - 1]
        ans2 = sum(abs(target2 - num) // x for num in nums)

        return min(ans1, ans2)
