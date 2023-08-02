"""
Leetcode
46. Permutations (medium)
2023-08-02

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

from typing import List


class Solution:
    """
    Runtime: 47 ms, faster than 89.92% of Python3 online submissions for Permutations.
    Memory Usage: 16.5 MB, less than 41.62% of Python3 online submissions for Permutations.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr_perm, arr):
            if not arr:
                ans.append(curr_perm)
                return

            for i in range(len(arr)):
                nxt_num = arr.pop(i)
                dfs(curr_perm + [nxt_num], arr)
                arr.insert(i, nxt_num)

        dfs([], nums)

        return ans


class Solution1:
    """
    leetcode solution: backtracking
    Time: O(n * n!)
    Space: O(n)
    Runtime: 40 ms, faster than 97.96% of Python3 online submissions for Permutations.
    Memory Usage: 16.3 MB, less than 91.96% of Python3 online submissions for Permutations.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans
