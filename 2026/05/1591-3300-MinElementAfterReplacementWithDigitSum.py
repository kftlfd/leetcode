"""
Leetcode
2026-05-29
3300. Minimum Element After Replacement With Digit Sum
Easy

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 

Example 1:

Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:

Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 10^4


"""

from typing import List


class Solution:
    """
    Runtime 3ms Beats 80.35%
    Memory 19.26MB Beats 56.38%
    """

    def minElement(self, nums: List[int]) -> int:

        def get_digit_sum(num: int) -> int:
            out = 0
            while num > 0:
                num, rem = divmod(num, 10)
                out += rem
            return out

        return min(map(get_digit_sum, nums))


class Solution1:
    """
    leetcode solution
    Runtime 3ms Beats 80.35%
    Memory 19.30MB Beats 56.38%
    """

    def minElement(self, nums: List[int]) -> int:
        ans = 37
        for num in nums:
            dig = 0
            while num > 0:
                dig += num % 10
                num //= 10
            ans = min(ans, dig)
        return ans
