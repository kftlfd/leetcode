"""
Leetcode
377. Combination Sum IV (medium)
2023-09-09

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All the elements of nums are unique.
    1 <= target <= 1000
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question 
    Runtime: 47 ms, faster than 60.38% of Python3 online submissions for Combination Sum IV.
    Memory Usage: 16.3 MB, less than 61.53% of Python3 online submissions for Combination Sum IV.
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        combs = [0] * (target + 1)
        # if target can = 0: combs[0] = 1

        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    combs[i] += 1
                if num < i:
                    combs[i] += combs[i - num]

        return combs[target]


s = Solution()
tests = [
    (([1, 2, 3], 4),
     7),

    (([9], 3),
     0),
]
for inp, exp in tests:
    res = s.combinationSum4(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
