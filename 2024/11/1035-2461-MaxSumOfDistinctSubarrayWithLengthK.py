"""
Leetcode
2024-11-19
2461. Maximum Sum of Distinct Subarrays With Length K
Medium

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

    The length of the subarray is k, and
    All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

 

Constraints:

    1 <= k <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
"""

from collections import Counter
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = k
        ans = 0
        window = Counter(nums[:k])
        window_sum = sum(nums[:k])

        while True:
            ans = max(ans, window_sum if all(
                v <= 1 for v in window.values()) else 0)

            right += 1
            if right >= n:
                break

            window_sum += nums[right] - nums[left]
            window[nums[right]] += 1
            window[nums[left]] -= 1
            left += 1

        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 127 ms, faster than 49.05% of Python3 online submissions for Maximum Sum of Distinct Subarrays With Length K.
    Memory Usage: 36.8 MB, less than 6.50% of Python3 online submissions for Maximum Sum of Distinct Subarrays With Length K.
    """

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        begin = 0
        end = 0
        num_to_index = {}

        while end < len(nums):
            curr_num = nums[end]
            last_occurrence = num_to_index.get(curr_num, -1)
            # if current window already has number or if window is too big, adjust window
            while begin <= last_occurrence or end - begin + 1 > k:
                current_sum -= nums[begin]
                begin += 1
            num_to_index[curr_num] = end
            current_sum += nums[end]
            if end - begin + 1 == k:
                ans = max(ans, current_sum)
            end += 1
        return ans


s = Solution()
tests = [
    (([1, 5, 4, 2, 9, 9, 9], 3),
     15),

    (([4, 4, 4], 3),
     0),
]
for inp, exp in tests:
    res = s.maximumSubarraySum(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
