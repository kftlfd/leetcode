"""
Leetcode
2025-07-28
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


Hint 1
Can we enumerate all possible subsets?
Hint 2
The maximum bitwise-OR is the bitwise-OR of the whole array.
"""

from typing import List


class Solution:
    """
    Runtime 1582ms Beats 6.51%
    Memory 17.80MB Beats 55.19%
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)

        max_or = 0
        for num in nums:
            max_or |= num

        def get_subset_or(mask: int) -> int:
            out = 0
            i = 0
            m = 1
            while i < n:
                if m & mask == m:
                    out |= nums[i]
                i += 1
                m <<= 1
            return out

        return sum(get_subset_or(m) == max_or for m in range(1 << n))


class Solution1:
    """
    leetcode solution 1: Recursion
    Runtime 234ms Beats 69.45%
    Memory 17.87MB Beats 55.19%
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(
        self, nums: List[int], index: int, current_or: int, target_or: int
    ) -> int:
        # Base case: reached the end of the array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Don't include the current number
        count_without = self._count_subsets(
            nums, index + 1, current_or, target_or
        )

        # Include the current number
        count_with = self._count_subsets(
            nums, index + 1, current_or | nums[index], target_or
        )

        # Return the sum of both cases
        return count_without + count_with


class Solution2:
    """
    leetcode solution 2: Memoization
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        n = len(nums)

        # Calculate the maximum OR value
        for num in nums:
            max_or_value |= num

        # Initialize memo with -1
        memo = [[-1] * (max_or_value + 1) for _ in range(n)]

        return self._count_subsets_recursive(nums, 0, 0, max_or_value, memo)

    def _count_subsets_recursive(
        self,
        nums: List[int],
        index: int,
        current_or: int,
        target_or: int,
        memo: List[List[int]],
    ) -> int:
        # Base case: reached the end of the array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Check if the result for this state is already memoized
        if memo[index][current_or] != -1:
            return memo[index][current_or]

        # Don't include the current number
        count_without = self._count_subsets_recursive(
            nums, index + 1, current_or, target_or, memo
        )

        # Include the current number
        count_with = self._count_subsets_recursive(
            nums, index + 1, current_or | nums[index], target_or, memo
        )

        # Memoize and return the result
        memo[index][current_or] = count_without + count_with
        return memo[index][current_or]


class Solution3:
    """
    leetcode solution 3: Bit Manipulation
    Runtime 1327ms Beats 12.42%
    Memory 17.62MB Beats 90.63%
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum possible OR value
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        total_subsets = 1 << len(nums)  # 2^n subsets
        subsets_with_max_or = 0

        # Iterate through all possible subsets
        for subset_mask in range(total_subsets):
            current_or_value = 0

            # Calculate OR value for the current subset
            for i in range(len(nums)):
                if (subset_mask >> i) & 1:
                    current_or_value |= nums[i]

            # If current subset's OR equals max_or_value, increment count
            if current_or_value == max_or_value:
                subsets_with_max_or += 1

        return subsets_with_max_or


class Solution4:
    """
    leetcode solution 4: Bit Manipulation + Dynamic Programming
    Runtime 2896ms Beats 5.09%
    Memory 18.88MB Beats 16.29%
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
