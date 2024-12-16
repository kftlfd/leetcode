"""
Leetcode
2024-12-16
3264. Final Array State After K Multiplication Operations I
Easy

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

    Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
    Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing all k operations.

 

Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:
Operation 	Result
After operation 1 	[2, 2, 3, 5, 6]
After operation 2 	[4, 2, 3, 5, 6]
After operation 3 	[4, 4, 3, 5, 6]
After operation 4 	[4, 4, 6, 5, 6]
After operation 5 	[8, 4, 6, 5, 6]

Example 2:

Input: nums = [1,2], k = 3, multiplier = 4

Output: [16,8]

Explanation:
Operation 	Result
After operation 1 	[4, 2]
After operation 2 	[4, 8]
After operation 3 	[16, 8]

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100
    1 <= k <= 10
    1 <= multiplier <= 5
"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    """
    Runtime: 3 ms, faster than 52.21% of Python3 online submissions for Final Array State After K Multiplication Operations I.
    Memory Usage: 17.5 MB, less than 11.77% of Python3 online submissions for Final Array State After K Multiplication Operations I.
    """

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(num, i) for i, num in enumerate(nums)]
        heapify(h)

        for _ in range(k):
            num, i = heappop(h)
            heappush(h, (num*multiplier, i))

        return [v[0] for v in sorted(h, key=lambda x: x[1])]


class Solution1:
    """
    leetcode solution
    Runtime: 4 ms, faster than 26.48% of Python3 online submissions for Final Array State After K Multiplication Operations I.
    Memory Usage: 17.3 MB, less than 28.27% of Python3 online submissions for Final Array State After K Multiplication Operations I.
    """

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums = nums[:]

        h = [(num, i) for i, num in enumerate(nums)]
        heapify(h)

        for _ in range(k):
            _, i = heappop(h)
            nums[i] *= multiplier
            heappush(h, (nums[i], i))

        return nums
