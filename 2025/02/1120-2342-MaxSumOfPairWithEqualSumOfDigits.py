"""
Leetcode
2025-02-12
2342. Max Sum of a Pair With Equal Sum of Digits
Medium
Topics
Companies
Hint

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9

Hint 1
What is the largest possible sum of digits a number can have?
Hint 2
Group the array elements by the sum of their digits, and find the largest two elements of each group.
"""

from collections import defaultdict
import heapq
from typing import List


class Solution:
    """
    Runtime 547ms Beats 19.03%
    Memory 33.06MB Beats 90.74%
    """

    def maximumSum(self, nums: List[int]) -> int:

        def digits_sum(num: int) -> int:
            return sum(int(d) for d in str(num))

        digit_sums = defaultdict(list)

        for num in nums:
            digit_sums[digits_sum(num)].append(num)

        ans = -1

        for group in digit_sums.values():
            if len(group) < 2:
                continue
            ans = max(ans, sum(sorted(group, reverse=True)[:2]))

        return ans


class Solution1:
    """
    leetcode solution 1: Sorting
    Runtime 507ms Beats 25.72%
    Memory 38.76MB Beats 5.56%
    """

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_pairs = []

        # Store numbers with their digit sums as pairs
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))

        # Sort based on digit sums, and if equal, by number value
        digit_sum_pairs.sort()

        max_pair_sum = -1

        # Iterate through the sorted array to find the maximum sum of pairs
        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            # If two consecutive numbers have the same digit sum
            if current_digit_sum == previous_digit_sum:
                current_sum = (
                    digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                )
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum

    # Helper function to compute the sum of digits of a number
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum


class Solution2:
    """
    leetcode solution 2: Priority Queue
    Runtime 258ms Beats 93.93%
    Memory 33.56MB Beats 69.14%
    """

    def maximumSum(self, nums: List[int]) -> int:
        # List to store a heap for each possible digit sum (0 to 81)
        digit_sum_groups = [[] for _ in range(82)]

        max_pair_sum = -1

        # Group numbers by their digit sums, maintaining heap size of 2
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            heapq.heappush(digit_sum_groups[digit_sum], number)

            # Keep only the top 2 largest numbers in the heap
            if len(digit_sum_groups[digit_sum]) > 2:
                heapq.heappop(
                    digit_sum_groups[digit_sum]
                )  # Remove the smallest element

        # Traverse the list to find the maximum pair sum for each group
        for min_heap in digit_sum_groups:
            if len(min_heap) == 2:
                first = heapq.heappop(min_heap)
                second = heapq.heappop(min_heap)
                max_pair_sum = max(max_pair_sum, first + second)

        return max_pair_sum

    # Helper function to compute the sum of digits of a number
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum


class Solution3:
    """
    leetcode solution 3: Store Maximum Value
    Runtime 340ms Beats 57.10%
    Memory 33.52MB Beats 69.14%
    """

    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        # Array to map digit sums to the largest element with that sum
        # (82 to cover all possible sums from 0 to 81)
        digit_mapping = [0] * 82

        for element in nums:
            digit_sum = 0
            # Calculating digit sum
            temp_element = element
            while temp_element:
                # Extract the last digit and add it to digit sum
                temp_element, curr_digit = divmod(temp_element, 10)
                digit_sum += curr_digit

            # Check if there is already an element with the same digit sum
            if digit_mapping[digit_sum] > 0:
                # Update the result if the sum of the current and mapped element is greater
                result = max(result, digit_mapping[digit_sum] + element)

            # Update the mapping to store the larger of the current or previous element for this digit sum
            digit_mapping[digit_sum] = max(digit_mapping[digit_sum], element)

        return result
