"""
Leetcode
2024-09-18
179. Largest Number
Medium

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    """
    wrong solution
    """

    def largestNumber(self, nums: List[int]) -> str:
        def to_key(i: int) -> str:
            k = str(i)
            if len(k) < 10:
                k += k[-1] * (10 - len(k))
            return int(k)

        return "".join(str(n) for n in sorted(nums, key=to_key, reverse=True))


class Solution1:
    """
    leetcode solution
    Runtime: 34 ms, faster than 91.12% of Python3 online submissions for Largest Number.
    Memory Usage: 16.5 MB, less than 74.54% of Python3 online submissions for Largest Number.
    """

    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)


s = Solution()
tests = [
    ([34323, 3432],
     "343234323"),
]
for inp, exp in tests:
    res = s.largestNumber(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
