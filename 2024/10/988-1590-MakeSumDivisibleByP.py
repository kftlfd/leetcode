"""
Leetcode
2024-10-03
1590. Make Sum Divisible by P
Medium

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= p <= 10^9

Hints:
- Use prefix sums to calculate the subarray sums.
- Suppose you know the remainder for the sum of the entire array. How does removing a subarray affect that remainder? What remainder does the subarray need to have in order to make the rest of the array sum up to be divisible by k?
- Use a map to keep track of the rightmost index for every prefix sum % p.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

        sums = [0] * (n + 1)
        for i, num in enumerate(nums):
            sums[i + 1] = num + sums[i]

        rem = sums[-1] % p

        if rem == 0:
            return 0

        for subarr_len in range(1, n):
            for start in range(n - subarr_len + 1):
                # subarr_sum = sum(nums[start:start+subarr_len])
                subarr_sum = sums[start+subarr_len] - sums[start]
                if subarr_sum % p == rem:
                    return subarr_len

        return -1


class Solution2:
    """
    leetcode solution 2: Prefix Sum Modulo
    Runtime: 422 ms, faster than 14.71% of Python3 online submissions for Make Sum Divisible by P.
    Memory Usage: 34.9 MB, less than 76.09% of Python3 online submissions for Make Sum Divisible by P.
    """

    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0

        # Step 1: Calculate total sum and target remainder
        for num in nums:
            total_sum = (total_sum + num) % p

        target = total_sum % p
        if target == 0:
            return 0  # The array is already divisible by p

        # Step 2: Use a dict to track prefix sum mod p
        mod_map = {
            0: -1
        }  # To handle the case where the whole prefix is the answer
        current_sum = 0
        min_len = n

        # Step 3: Iterate over the array
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p

            # Calculate what we need to remove
            needed = (current_sum - target + p) % p

            # If we have seen the needed remainder, we can consider this subarray
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            # Store the current remainder and index
            mod_map[current_sum] = i

        # Step 4: Return result
        return -1 if min_len == n else min_len
