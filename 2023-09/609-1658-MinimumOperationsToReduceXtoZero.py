"""
Leetcode
1658. Minimum Operations to Reduce X to Zero (medium)
2023-09-20

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
    1 <= x <= 10^9
"""

from itertools import accumulate
from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016199/Python-O(n)-solution-using-cumulative-sums
    Runtime: 1019 ms, faster than 40.32% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
    Memory Usage: 38.8 MB, less than 7.26% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
    """

    def minOperations(self, nums: List[int], x: int) -> int:
        cumsum = [0] + list(accumulate(nums))
        dic = {c: i for i, c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0:
            return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1
