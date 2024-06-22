"""
Leetcode
1248. Count Number of Nice Subarrays
Medium
2024-06-22

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

 

Constraints:

    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length
"""

from collections import deque
from typing import List


class Solution1:
    """
    leetcode solution 1: Hashing
    Runtime: 608 ms, faster than 64.65% of Python3 online submissions for Count Number of Nice Subarrays.
    Memory Usage: 23.4 MB, less than 84.95% of Python3 online submissions for Count Number of Nice Subarrays.
    """

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum: 1}

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            # Find subarrays with sum k ending at i
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            # Increment the current prefix sum in hashmap
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return subarrays


class Solution2:
    """
    leetcode solution 2: Sliding Window using Queue
    Runtime: 590 ms, faster than 76.16% of Python3 online submissions for Count Number of Nice Subarrays.
    Memory Usage: 23.2 MB, less than 93.79% of Python3 online submissions for Count Number of Nice Subarrays.
    """

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = deque()
        subarrays = 0
        last_popped = -1
        initial_gap = -1

        for i in range(len(nums)):
            # If element is odd, append its index to the deque.
            if nums[i] % 2 == 1:
                odd_indices.append(i)
            # If the number of odd numbers exceeds k, remove the first odd index.
            if len(odd_indices) > k:
                last_popped = odd_indices.popleft()
            # If there are exactly k odd numbers, add the number of even numbers
            # in the beginning of the subarray to the result.
            if len(odd_indices) == k:
                initial_gap = odd_indices[0] - last_popped
                subarrays += initial_gap

        return subarrays


class Solution3:
    """
    leetcode solution 3: Sliding Window (Space Optimized)
    Runtime: 565 ms, faster than 92.88% of Python3 online submissions for Count Number of Nice Subarrays.
    Memory Usage: 23.6 MB, less than 42.15% of Python3 online submissions for Count Number of Nice Subarrays.
    """

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = 0
        initial_gap = 0
        qsize = 0
        start = 0
        for end in range(len(nums)):
            # If current element is odd, increment qsize by 1.
            if nums[end] % 2 == 1:
                qsize += 1
            if qsize == k:
                initial_gap = 0
                # Calculate the number of even elements in the beginning of
                # subarray.
                while qsize == k:
                    qsize -= nums[start] % 2
                    initial_gap += 1
                    start += 1
            subarrays += initial_gap
        return subarrays


class Solution4:
    """
    leetcode solution 4: Sliding Window (subarray sum at most k)
    Runtime: 644 ms, faster than 32.46% of Python3 online submissions for Count Number of Nice Subarrays.
    Memory Usage: 23.4 MB, less than 91.48% of Python3 online submissions for Count Number of Nice Subarrays.
    """

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums: List[int], k: int) -> int:
        window_size, subarrays, start = 0, 0, 0
        for end in range(len(nums)):
            window_size += nums[end] % 2
            # Find the first index start where the window has exactly k odd elements.
            while window_size > k:
                window_size -= nums[start] % 2
                start += 1
            # Increment number of subarrays with end - start + 1.
            subarrays += end - start + 1
        return subarrays
