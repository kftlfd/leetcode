"""
Leetcode
78. Subsets
Medium
2024-05-21

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""

from typing import List


class Solution:
    """
    Runtime: 29 ms, faster than 93.95% of Python3 online submissions for Subsets.
    Memory Usage: 16.8 MB, less than 30.01% of Python3 online submissions for Subsets.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]

        def recurse(cur, i, pick):
            if i >= n:
                return

            if pick:
                cur.append(nums[i])
                ans.append(cur[:])

            recurse(cur, i+1, False)
            recurse(cur, i+1, True)

            if pick:
                cur.pop()

        recurse([], -1, False)

        return ans


class Solution1:
    """
    sample 23 ms submission
    Runtime: 39 ms, faster than 44.69% of Python3 online submissions for Subsets.
    Memory Usage: 16.7 MB, less than 77.55% of Python3 online submissions for Subsets.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subset(current, nxt):
            res.append(current)

            for i in range(len(nxt)):
                subset(current + [nxt[i]], nxt[i+1:])

        subset([], nums)

        return res
