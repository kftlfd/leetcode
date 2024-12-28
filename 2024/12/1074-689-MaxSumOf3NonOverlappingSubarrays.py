"""
Leetcode
2024-12-28
689. Maximum Sum of 3 Non-Overlapping Subarrays
Hard

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

 

Constraints:

    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] < 2^16
    1 <= k <= floor(nums.length / 3)
"""

from itertools import accumulate
from typing import List


class Solution1:
    """
    leetcode solution 1: memoization
    """

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Number of possible subarray starting positions
        n = len(nums) - k + 1

        # Calculate sum of all possible k-length subarrays
        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        # memo[i][j]: max sum possible starting from index i with j subarrays remaining
        memo = [[-1] * 4 for _ in range(n)]
        indices = []

        # First find optimal sum using DP
        self._dp(sums, k, 0, 3, memo)

        # Then reconstruct the path to find indices
        self._dfs(sums, k, 0, 3, memo, indices)

        return indices

    def _dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0
        if idx >= len(sums):
            return float("-inf") if rem > 0 else 0

        if memo[idx][rem] != -1:
            return memo[idx][rem]

        # Try taking current subarray vs skipping it
        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        memo[idx][rem] = max(with_current, skip_current)
        return memo[idx][rem]

    def _dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return

        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        # Choose path that gave optimal result in DP
        if with_current >= skip_current:  # Take current subarray
            indices.append(idx)
            self._dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:  # Skip current subarray
            self._dfs(sums, k, idx + 1, rem, memo, indices)


class Solution2:
    """
    leetcode solution 2: Tabulation
    """

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Number of possible subarray starting positions
        n = len(nums) - k + 1

        # Calculate sum of all possible k-length subarrays
        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        # memo[i][j]: max sum possible starting from index i with j subarrays remaining
        memo = [[-1] * 4 for _ in range(n)]
        indices = []

        # First find optimal sum using DP
        self._dp(sums, k, 0, 3, memo)

        # Then reconstruct the path to find indices
        self._dfs(sums, k, 0, 3, memo, indices)

        return indices

    def _dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0
        if idx >= len(sums):
            return float("-inf") if rem > 0 else 0

        if memo[idx][rem] != -1:
            return memo[idx][rem]

        # Try taking current subarray vs skipping it
        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        memo[idx][rem] = max(with_current, skip_current)
        return memo[idx][rem]

    def _dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return

        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        # Choose path that gave optimal result in DP
        if with_current >= skip_current:  # Take current subarray
            indices.append(idx)
            self._dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:  # Skip current subarray
            self._dfs(sums, k, idx + 1, rem, memo, indices)


class Solution3:
    """
    leetcode solution 3: Three Pointers
    """

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_sum = 0

        # Create prefix sum array using accumulate
        prefix_sum = [0] + list(accumulate(nums))

        # Initialize arrays for best indices
        left_max_idx = [0] * n
        right_max_idx = [0] * n
        result = [0] * 3

        # Calculate best left subarray positions
        curr_max_sum = prefix_sum[k] - prefix_sum[0]
        for i in range(k, n):
            curr_sum = prefix_sum[i + 1] - prefix_sum[i + 1 - k]
            if curr_sum > curr_max_sum:
                left_max_idx[i] = i + 1 - k
                curr_max_sum = curr_sum
            else:
                left_max_idx[i] = left_max_idx[i - 1]

        # Calculate best right subarray positions
        right_max_idx[n - k] = n - k
        curr_max_sum = prefix_sum[n] - prefix_sum[n - k]
        for i in range(n - k - 1, -1, -1):
            curr_sum = prefix_sum[i + k] - prefix_sum[i]
            if curr_sum >= curr_max_sum:
                right_max_idx[i] = i
                curr_max_sum = curr_sum
            else:
                right_max_idx[i] = right_max_idx[i + 1]

        # Find optimal middle position
        for i in range(k, n - 2 * k + 1):
            left_idx = left_max_idx[i - 1]
            right_idx = right_max_idx[i + k]
            total_sum = (
                prefix_sum[i + k]
                - prefix_sum[i]
                + prefix_sum[left_idx + k]
                - prefix_sum[left_idx]
                + prefix_sum[right_idx + k]
                - prefix_sum[right_idx]
            )

            if total_sum > max_sum:
                max_sum = total_sum
                result = [left_idx, i, right_idx]

        return result


class Solution4:
    """
    leetcode solution 4: Sliding Window
    """

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Variables to track the best indices for one, two, and three subarray configurations
        best_single_start = 0
        best_double_start = [0, k]
        best_triple_start = [0, k, k * 2]

        # Compute the initial sums for the first three subarrays
        current_window_sum_single = sum(nums[:k])
        current_window_sum_double = sum(nums[k: k * 2])
        current_window_sum_triple = sum(nums[k * 2: k * 3])

        # Track the best sums found so far
        best_single_sum = current_window_sum_single
        best_double_sum = current_window_sum_single + current_window_sum_double
        best_triple_sum = (
            current_window_sum_single
            + current_window_sum_double
            + current_window_sum_triple
        )

        # Sliding window pointers for the subarrays
        single_start_index = 1
        double_start_index = k + 1
        triple_start_index = k * 2 + 1

        # Slide the windows across the array
        while triple_start_index <= len(nums) - k:
            # Update the sums using the sliding window technique
            current_window_sum_single = (
                current_window_sum_single
                - nums[single_start_index - 1]
                + nums[single_start_index + k - 1]
            )
            current_window_sum_double = (
                current_window_sum_double
                - nums[double_start_index - 1]
                + nums[double_start_index + k - 1]
            )
            current_window_sum_triple = (
                current_window_sum_triple
                - nums[triple_start_index - 1]
                + nums[triple_start_index + k - 1]
            )

            # Update the best single subarray start index if a better sum is found
            if current_window_sum_single > best_single_sum:
                best_single_start = single_start_index
                best_single_sum = current_window_sum_single

            # Update the best double subarray start indices if a better sum is found
            if current_window_sum_double + best_single_sum > best_double_sum:
                best_double_start[0] = best_single_start
                best_double_start[1] = double_start_index
                best_double_sum = current_window_sum_double + best_single_sum

            # Update the best triple subarray start indices if a better sum is found
            if current_window_sum_triple + best_double_sum > best_triple_sum:
                best_triple_start[0] = best_double_start[0]
                best_triple_start[1] = best_double_start[1]
                best_triple_start[2] = triple_start_index
                best_triple_sum = current_window_sum_triple + best_double_sum

            # Move the sliding windows forward
            single_start_index += 1
            double_start_index += 1
            triple_start_index += 1

        # Return the starting indices of the three subarrays with the maximum sum
        return best_triple_start
