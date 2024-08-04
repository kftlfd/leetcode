"""
Leetcode
1508. Range Sum of Sorted Subarray Sums
Medium
2024-08-04

You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 

Example 2:

Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.

Example 3:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50

 

Constraints:

    n == nums.length
    1 <= nums.length <= 1000
    1 <= nums[i] <= 100
    1 <= left <= right <= n * (n + 1) / 2
"""

import heapq
from typing import List


class Solution:
    """
    Runtime: 232 ms, faster than 50.88% of Python3 online submissions for Range Sum of Sorted Subarray Sums.
    Memory Usage: 39.8 MB, less than 60.62% of Python3 online submissions for Range Sum of Sorted Subarray Sums.
    """

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(list(sorted(self.subarray_sums(nums)))[left-1:right]) % (10**9 + 7)

    def subarray_sums(self, nums: list[int]):
        n = len(nums)
        for l in range(n):
            cur_sum = nums[l]
            yield cur_sum
            for r in range(l + 1,  n):
                cur_sum += nums[r]
                yield cur_sum


class Solution2:
    """
    leetcode solution 2: Priority Queue
    Runtime: 288 ms, faster than 25.66% of Python3 online submissions for Range Sum of Sorted Subarray Sums.
    Memory Usage: 16.8 MB, less than 93.81% of Python3 online submissions for Range Sum of Sorted Subarray Sums.
    """

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], i))

        ans = 0
        mod = 1e9 + 7
        for i in range(1, right + 1):
            p = heapq.heappop(pq)
            # If the current index is greater than or equal to left, add the
            # value to the answer.
            if i >= left:
                ans = (ans + p[0]) % mod
            # If index is less than the last index, increment it and add its
            # value to the first pair value.
            if p[1] < n - 1:
                p = (p[0] + nums[p[1] + 1], p[1] + 1)
                heapq.heappush(pq, p)

        return int(ans)


class Solution3:
    """
    leetcode solution 3: Binary Search and Sliding Window
    Runtime: 62 ms, faster than 98.23% of Python3 online submissions for Range Sum of Sorted Subarray Sums.
    Memory Usage: 16.6 MB, less than 97.79% of Python3 online submissions for Range Sum of Sorted Subarray Sums.
    """

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                current_sum += nums[j]
                window_sum += nums[j] * (j - i + 1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return count, total_sum

        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            max_sum = sum(nums)
            left = min_sum
            right = max_sum

            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            count, total_sum = count_and_sum(nums, n, left)
            # There can be more subarrays with the same sum of left.
            return total_sum - left * (count - k)

        result = (
            sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)
        ) % mod
        # Ensure non-negative result
        return (result + mod) % mod
