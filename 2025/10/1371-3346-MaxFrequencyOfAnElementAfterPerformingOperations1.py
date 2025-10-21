"""
Leetcode
2025-10-21
3346. Maximum Frequency of an Element After Performing Operations I
Medium

You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

    Select an index i that was not selected in any previous operations.
    Add an integer in the range [-k, k] to nums[i].

Return the maximum possible

of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

    Adding 0 to nums[1]. nums becomes [1, 4, 5].
    Adding -1 to nums[2]. nums becomes [1, 4, 4].

Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

    Adding 0 to nums[1].

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    0 <= k <= 10^5
    0 <= numOperations <= nums.length


Hint 1
Sort the array and try each value in range as a candidate.
"""

import bisect
from typing import List


class Solution:
    """
    leetcode solution: Sort + Enumerate + Binary Search
    Runtime 599ms Beats 60.46%
    Memory 33.42MB Beats 62.21%
    """

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        num_count = {}
        last_num_index = 0
        for i in range(n):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)

        for i in range(nums[0], nums[-1] + 1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)

        return ans
