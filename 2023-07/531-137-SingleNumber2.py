"""
Leetcode
137. Single Number II (medium)
2023-07-04

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,3,2]
Output: 3

Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:

    1 <= nums.length <= 3 * 104
    -231 <= nums[i] <= 231 - 1
    Each element in nums appears exactly three times except for one element which appears once.
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/single-number-ii/discuss/699889/Python-Bit-Manipulation-O(32n)-but-easy-exaplained
    Runtime: 153 ms, faster than 25.83% of Python3 online submissions for Single Number II.
    Memory Usage: 18 MB, less than 98.16% of Python3 online submissions for Single Number II.
    """

    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i) == (1 << i):
                    count += 1
            ans |= (count % 3) << i

        return ans if ans < (1 << 31) else ans - (1 << 32)


class Solution1:
    """
    https://leetcode.com/problems/single-number-ii/discuss/3714928/Bit-Manipulation-oror-C++-oror-JAVA-oror-PYTHON-oror-Beginner-Friendly
    Runtime: 67 ms, faster than 90.95% of Python3 online submissions for Single Number II.
    Memory Usage: 18 MB, less than 98.16% of Python3 online submissions for Single Number II.
    """

    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones


s = Solution1()
tests = [
    ([2, 2, 3, 2],
     3),

    ([0, 1, 0, 1, 0, 1, 99],
     99),
]
for inp, exp in tests:
    res = s.singleNumber(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
