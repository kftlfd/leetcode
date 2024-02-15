"""
Leetcode
2971. Find Polygon With the Largest Perimeter
Medium
2024-02-15

You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.

 

Example 1:

Input: nums = [5,5,5]
Output: 15
Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.

Example 2:

Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.

Example 3:

Input: nums = [5,5,50]
Output: -1
Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.

 

Constraints:

    3 <= n <= 105
    1 <= nums[i] <= 109
"""

from itertools import accumulate
from typing import List


class Solution:
    """
    Runtime: 524 ms, faster than 64.69% of Python3 online submissions for Find Polygon With the Largest Perimeter.
    Memory Usage: 31.6 MB, less than 83.74% of Python3 online submissions for Find Polygon With the Largest Perimeter.
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sums = list(accumulate(nums))

        for i in range(len(nums) - 1, 1, -1):
            largest = nums[i]
            prevsum = sums[i - 1]
            if largest < prevsum:
                return prevsum + largest

        return -1


class Solution1:
    """
    leetcode solution
    Runtime: 525 ms, faster than 63.92% of Python3 online submissions for Find Polygon With the Largest Perimeter.
    Memory Usage: 31.5 MB, less than 91.17% of Python3 online submissions for Find Polygon With the Largest Perimeter.
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        previous_elements_sum = 0
        ans = -1

        for num in nums:
            if num < previous_elements_sum:
                ans = num + previous_elements_sum
            previous_elements_sum += num

        return ans


s = Solution()
tests = [
    ([5, 5, 5],
     15),

    ([1, 12, 1, 2, 5, 50, 3],
     12),

    ([5, 5, 50],
     -1),
]
for inp, exp in tests:
    res = s.largestPerimeter(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
