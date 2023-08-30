"""
Leetcode
2366. Minimum Replacements to Sort the Array (hard)
2023-08-30

You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

    For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].

Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Example 1:

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""

from typing import List, Tuple
from math import ceil


class Solution:
    """
    Wrong Answer
    """

    def minimumReplacement(self, nums: List[int]) -> int:

        def replace(num: int, r_bound: int) -> Tuple[int, int]:
            """return (number of replacements, new right bound)"""

            if num <= r_bound:
                return (0, num)

            operations = ceil(num / r_bound) - 1

            rem = num % r_bound
            n_r_bound = (r_bound + rem if rem else 2 * r_bound) // 2

            return (operations, n_r_bound)

        ans = 0
        right_bound = nums[-1]
        for num in nums[-2::-1]:
            replacements, new_right_bound = replace(num, right_bound)
            ans += replacements
            right_bound = new_right_bound

        return ans


class Solution1:
    """
    fixed after seeing leetcode solution
    Runtime: 479 ms, faster than 76.86% of Python3 online submissions for Minimum Replacements to Sort the Array.
    Memory Usage: 31.2 MB, less than 73.55% of Python3 online submissions for Minimum Replacements to Sort the Array.
    """

    def minimumReplacement(self, nums: List[int]) -> int:

        def replace(num: int, r_bound: int) -> Tuple[int, int]:
            """return (number of replacements, new right bound)"""

            if num <= r_bound:
                return (0, num)

            elements = (num + r_bound - 1) // r_bound

            operations = elements - 1

            n_r_bound = num // elements

            return (operations, n_r_bound)

        ans = 0
        right_bound = nums[-1]
        for num in nums[-2::-1]:
            replacements, new_right_bound = replace(num, right_bound)
            ans += replacements
            right_bound = new_right_bound

        return ans


class Solution2:
    """
    leetcode solution
    Runtime: 491 ms, faster than 67.77% of Python3 online submissions for Minimum Replacements to Sort the Array.
    Memory Usage: 28 MB, less than 89.26% of Python3 online submissions for Minimum Replacements to Sort the Array.
    """

    def minimumReplacement(self, nums: List[int]) -> int:

        answer = 0
        n = len(nums)

        # Start from the second last element, as the last one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue

            # Count how many elements are made from breaking nums[i].
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            # It requires numElements - 1 replacement operations.
            answer += num_elements - 1

            # Maximize nums[i] after replacement.
            nums[i] = nums[i] // num_elements

        return answer


s = Solution()
tests = [
    ([3, 9, 3],
     2),

    ([1, 2, 3, 4, 5],
     0),

    ([6, 5],
     1),

    ([2, 10, 3],
     3),
]
for inp, exp in tests:
    res = s.minimumReplacement(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
