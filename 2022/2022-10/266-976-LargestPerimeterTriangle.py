"""
Leetcode
976. Largest Perimeter Triangle (easy)
2022-10-12

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0
"""

from typing import List, Optional


# bruteforce
# Runtime: 839 ms, faster than 5.00% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 15.5 MB, less than 8.94% of Python3 online submissions for Largest Perimeter Triangle.
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        def is_valid_triangle(a, b, c):
            return (a < b+c) and (b < a+c) and (c < a+b)

        sides = sorted(nums, key=lambda x: -x)
        l = len(sides)
        for i in range(l-2):
            a = sides[i]
            for j in range(i+1, l-1):
                b = sides[j]
                c = sides[j+1]
                if is_valid_triangle(a, b, c):
                    return a + b + c

        return 0


# leetcode solution
# Runtime: 208 ms, faster than 89.04% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 15.4 MB, less than 91.63% of Python3 online submissions for Largest Perimeter Triangle.
class Solution1:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0


s = Solution1()
tests = [
    ([3, 6, 2, 3], 8),
    ([2, 1, 2], 5),
    ([1, 2, 1], 0),
]
for inp, exp in tests:
    print(inp)
    res = s.largestPerimeter(inp)
    if res != exp:
        print("exp: ", exp)
        print("got: ", res)
    print()
