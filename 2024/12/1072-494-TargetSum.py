"""
Leetcode
2024-12-26
494. Target Sum
Medium

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1

 

Constraints:

    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(idx: int, cur_sum: int) -> int:
            if idx >= len(nums):
                return int(cur_sum == target)

            num = nums[idx]
            return dfs(idx + 1, cur_sum + num) + dfs(idx + 1, cur_sum - num)

        return dfs(0, 0)


class Solution2:
    """
    leetcode solution 2: Recursion with Memoization
    Runtime: 187 ms, faster than 35.82% of Python3 online submissions for Target Sum.
    Memory Usage: 18.3 MB, less than 59.08% of Python3 online submissions for Target Sum.
    """

    total_sum = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total_sum = sum(nums)
        memo = [
            [float("-inf")] * (2 * self.total_sum + 1) for _ in range(len(nums))
        ]
        return self.calculate_ways(nums, 0, 0, target, memo)

    def calculate_ways(
        self,
        nums: List[int],
        current_index: int,
        current_sum: int,
        target: int,
        memo: List[List[int]],
    ) -> int:
        if current_index == len(nums):
            # Check if the current sum matches the target
            return 1 if current_sum == target else 0
        else:
            # Check if the result is already computed
            if memo[current_index][current_sum + self.total_sum] != float(
                "-inf"
            ):
                return memo[current_index][current_sum + self.total_sum]

            # Calculate ways by adding the current number
            add = self.calculate_ways(
                nums,
                current_index + 1,
                current_sum + nums[current_index],
                target,
                memo,
            )

            # Calculate ways by subtracting the current number
            subtract = self.calculate_ways(
                nums,
                current_index + 1,
                current_sum - nums[current_index],
                target,
                memo,
            )

            # Store the result in memoization table
            memo[current_index][current_sum + self.total_sum] = add + subtract

            return memo[current_index][current_sum + self.total_sum]


class Solution3:
    """
    leetcode solution 3: 2D Dynamic Programming
    Runtime: 163 ms, faster than 60.74% of Python3 online submissions for Target Sum.
    Memory Usage: 18.2 MB, less than 60.47% of Python3 online submissions for Target Sum.
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # Initialize the first row of the DP table
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] += 1

        # Fill the DP table
        for index in range(1, len(nums)):
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[index - 1][sum_val + total_sum] > 0:
                    dp[index][sum_val + nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]
                    dp[index][sum_val - nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]

        # Return the result if the target is within the valid range
        return (
            0
            if abs(target) > total_sum
            else dp[len(nums) - 1][target + total_sum]
        )


class Solution4:
    """
    leetcode solution 4: Space Optimized
    Runtime: 123 ms, faster than 75.55% of Python3 online submissions for Target Sum.
    Memory Usage: 17.9 MB, less than 63.39% of Python3 online submissions for Target Sum.
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)

        # Initialize the first row of the DP table
        dp[nums[0] + total_sum] = 1  # Adding nums[0]
        dp[-nums[0] + total_sum] += 1  # Subtracting nums[0]

        # Fill the DP table
        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
                    next_dp[sum_val - nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
            dp = next_dp

        # Return the result if the target is within the valid range
        return 0 if abs(target) > total_sum else dp[target + total_sum]


class Solution5:
    """
    https://leetcode.com/problems/target-sum/solution/2776093
    Runtime: 103 ms, faster than 82.66% of Python3 online submissions for Target Sum.
    Memory Usage: 17.8 MB, less than 64.98% of Python3 online submissions for Target Sum.
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = defaultdict(int)
        d[0] = 1

        for num in nums:
            dp = defaultdict(int)
            for k, v in d.items():
                dp[k + num] += v
                dp[k - num] += v
            d = dp

        return d[target]
