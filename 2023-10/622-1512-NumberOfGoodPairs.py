"""
Leetcode
1512. Number of Good Pairs (easy)
2023-10-03

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

Hint:
Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
"""

from typing import List
from collections import Counter, defaultdict


class Solution:
    """
    Runtime: 44 ms, faster than 32.94% of Python3 online submissions for Number of Good Pairs.
    Memory Usage: 16.1 MB, less than 97.25% of Python3 online submissions for Number of Good Pairs.
    """

    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum(n * (n - 1) // 2 for n in count.values())


class Solution1:
    """
    leetcode solution
    Runtime: 36 ms, faster than 82.94% of Python3 online submissions for Number of Good Pairs.
    Memory Usage: 16.3 MB, less than 53.10% of Python3 online submissions for Number of Good Pairs.
    """

    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0

        for num in nums:
            ans += counts[num]
            counts[num] += 1

        return ans
