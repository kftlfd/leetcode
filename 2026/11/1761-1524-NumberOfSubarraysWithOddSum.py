"""
Leetcode
2026-11-15
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

 

"""


class Solution3:
    """
    leetcode solution 3: Prefix Sum with Odd-Even Counting
    Runtime 85ms Beats 47.26%
    Memory 24.34MB Beats 93.04%
    """

    def numOfSubarrays(self, arr: list[int]) -> int:
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
