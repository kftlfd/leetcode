"""
Leetcode
1464. Maximum Product of Two Elements in an Array
Easy
2023-12-12

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:

Input: nums = [3,7]
Output: 12

 

Constraints:

    2 <= nums.length <= 500
    1 <= nums[i] <= 10^3
"""

from typing import List


class Solution:
    """
    Runtime: 51 ms, faster than 85.19% of Python3 online submissions for Maximum Product of Two Elements in an Array.
    Memory Usage: 16.3 MB, less than 75.06% of Python3 online submissions for Maximum Product of Two Elements in an Array.
    """

    def maxProduct(self, nums: List[int]) -> int:
        num1 = nums[0]
        num2 = nums[1]

        if num2 > num1:
            num1, num2 = num2, num1

        for i in range(2, len(nums)):
            num = nums[i]
            if num > num1:
                num2 = num1
                num1 = num
            elif num > num2:
                num2 = num

        return (num1 - 1) * (num2 - 1)


s = Solution()
tests = [
    ([3, 4, 5, 2],
     12),

    ([1, 5, 4, 5],
     16),

    ([3, 7],
     12),
]
for inp, exp in tests:
    res = s.maxProduct(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
