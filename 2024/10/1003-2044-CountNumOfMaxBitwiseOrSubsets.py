"""
Leetcode
2024-10-18
2044. Count Number of Maximum Bitwise-OR Subsets
Medium

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]

 

Constraints:

    1 <= nums.length <= 16
    1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime: 1536 ms, faster than 8.92% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
    Memory Usage: 16.6 MB, less than 44.07% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        return sum(
            self.sub_arr_or(nums, i) == max_or
            for i in range(1, 1 << len(nums))
        )

    def sub_arr_or(self, nums: List[int], bit_selection: int) -> int:
        arr_or = 0
        i = len(nums) - 1
        while i >= 0:
            if bit_selection & 1:
                arr_or |= nums[i]
            bit_selection = bit_selection >> 1
            i -= 1
        return arr_or


class Solution4:
    """
    leetcode solution 4: Bit Manipulation + Dynamic Programming
    Runtime: 2856 ms, faster than 5.18% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
    Memory Usage: 17.7 MB, less than 24.36% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        dp = [0] * (1 << 17)

        # Initialize the empty subset
        dp[0] = 1

        # Iterate through each number in the input array
        for num in nums:
            for i in range(max_or_value, -1, -1):
                # For each existing subset, create a new subset by including the current number
                dp[i | num] += dp[i]

            # Update the maximum OR value
            max_or_value |= num

        return dp[max_or_value]


s = Solution()
tests = [
    ([3, 1],
     2),

    ([2, 2, 2],
     7),

    ([3, 2, 1, 5],
     6),
]
for inp, exp in tests:
    res = s.countMaxOrSubsets(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
