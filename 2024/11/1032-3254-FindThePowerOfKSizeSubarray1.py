"""
Leetcode
2024-11-16
3254. Find the Power of K-Size Subarrays I
Medium

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

    Its maximum element if all of its elements are consecutive and sorted in ascending order.
    -1 otherwise.

You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

Example 1:

Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:

There are 5 subarrays of nums of size 3:

    [1, 2, 3] with the maximum element 3.
    [2, 3, 4] with the maximum element 4.
    [3, 4, 3] whose elements are not consecutive.
    [4, 3, 2] whose elements are not sorted.
    [3, 2, 5] whose elements are not consecutive.

Example 2:

Input: nums = [2,2,2,2,2], k = 4

Output: [-1,-1]

Example 3:

Input: nums = [3,2,3,2,3,2], k = 2

Output: [-1,3,-1,3,-1]

 

Constraints:

    1 <= n == nums.length <= 500
    1 <= nums[i] <= 10^5
    1 <= k <= n
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime: 83 ms, faster than 13.30% of Python3 online submissions for Find the Power of K-Size Subarrays I.
    Memory Usage: 16.7 MB, less than 86.53% of Python3 online submissions for Find the Power of K-Size Subarrays I.
    """

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)

        for i in range(n - k + 1):
            power = nums[i]
            for j in range(1, k):
                if nums[i+j] - nums[i+j-1] == 1:
                    power = nums[i+j]
                else:
                    power = -1
                    break
            ans[i] = power

        return ans


class Solution2:
    """
    leetcode solution 2: Sliding Window with Deque
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find the Power of K-Size Subarrays I.
    Memory Usage: 16.8 MB, less than 55.71% of Python3 online submissions for Find the Power of K-Size Subarrays I.
    """

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = [-1] * (length - k + 1)
        index_deque = deque()

        for current_index in range(length):
            if index_deque and index_deque[0] < current_index - k + 1:
                index_deque.popleft()
            if (
                index_deque
                and nums[current_index] != nums[current_index - 1] + 1
            ):
                index_deque.clear()

            index_deque.append(current_index)

            if current_index >= k - 1:
                if len(index_deque) == k:
                    result[current_index - k + 1] = nums[index_deque[-1]]
                else:
                    result[current_index - k + 1] = -1

        return result


class Solution3:
    """
    leetcode solution 3: Optimized Via Counter
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find the Power of K-Size Subarrays I.
    Memory Usage: 16.8 MB, less than 55.71% of Python3 online submissions for Find the Power of K-Size Subarrays I.
    """

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums  # If k is 1, every single element is a valid subarray

        length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive_count = 1  # Count of consecutive elements

        for index in range(length - 1):
            if nums[index] + 1 == nums[index + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1  # Reset count if not consecutive

            # If we have enough consecutive elements, update the result
            if consecutive_count >= k:
                result[index - k + 2] = nums[index + 1]

        return result
