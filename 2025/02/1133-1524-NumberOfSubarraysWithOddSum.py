"""
Leetcode
2025-02-25
1524. Number of Sub-arrays With Odd Sum
Medium

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16

 

Constraints:

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 100


Hint 1
Can we use the accumulative sum to keep track of all the odd-sum sub-arrays ?
Hint 2
if the current accu sum is odd, we care only about previous even accu sums and vice versa.
"""

from typing import List


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Runtime 207ms Beats 5.11%
    Memory 26.05MB Beats 10.75%
    """

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)

        # Convert elements to 0 (even) or 1 (odd)
        for i in range(n):
            arr[i] %= 2

        # dp_even[i] represents the number of subarrays with an even sum ending
        # at index i. dp_odd[i] represents the number of subarrays with an odd
        # sum ending at index i
        dp_even, dp_odd = [0] * n, [0] * n

        # Initialization based on the last element
        # The last element is even
        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            # The last element is odd
            dp_odd[n - 1] = 1

        # Traverse the array in reverse
        for num in range(n - 2, -1, -1):
            if arr[num] == 1:
                # Odd element contributes to odd subarrays
                dp_odd[num] = (1 + dp_even[num + 1]) % MOD
                # Even element continues the pattern
                dp_even[num] = dp_odd[num + 1]
            else:
                # Even element contributes to even subarrays
                dp_even[num] = (1 + dp_even[num + 1]) % MOD
                # Odd element continues the pattern
                dp_odd[num] = dp_odd[num + 1]

        # Sum all the odd subarrays
        count = 0
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD

        return int(count)


class Solution3:
    """
    leetcode solution 3: Prefix Sum with Odd-Even Counting
    Runtime 79ms Beats 53.49%
    Memory 22.00MB Beats 43.01%
    """

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = prefix_sum = 0
        # even_count starts as 1 since the initial sum (0) is even
        odd_count = 0
        even_count = 1

        for num in arr:
            prefix_sum += num
            # If current prefix sum is even, add the number of odd subarrays
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                # If current prefix sum is odd, add the number of even
                # subarrays
                count += even_count
                odd_count += 1

            count %= MOD  # To handle large results

        return count
