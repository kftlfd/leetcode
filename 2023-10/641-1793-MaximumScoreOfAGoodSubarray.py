"""
Leetcode
1793. Maximum Score of a Good Subarray (hard)
2023-10-22

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 2 * 10^4
    0 <= k < nums.length
"""

from bisect import bisect_left
from typing import List
from math import inf


class Solution1:
    """
    leetcode solution 1: binary search
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 1221 ms, faster than 5.61% of Python3 online submissions for Maximum Score of a Good Subarray.
    Memory Usage: 27.3 MB, less than 46.94% of Python3 online submissions for Maximum Score of a Good Subarray.
    """

    def maximumScore(self, nums: List[int], k: int) -> int:

        def solve(nums, k):
            n = len(nums)
            left = [0] * k
            curr_min = inf
            for i in range(k - 1, -1, -1):
                curr_min = min(curr_min, nums[i])
                left[i] = curr_min

            right = []
            curr_min = inf
            for i in range(k, n):
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)

            ans = 0
            for j in range(len(right)):
                curr_min = right[j]
                i = bisect_left(left, curr_min)
                size = (k + j) - i + 1
                ans = max(ans, curr_min * size)

            return ans

        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))


class Solution2:
    """
    leetcode solution 2: monotonic stack
    Time: O(n)
    Space: O(n)
    Runtime: 1111 ms, faster than 27.04% of Python3 online submissions for Maximum Score of a Good Subarray.
    Memory Usage: 26.8 MB, less than 84.18% of Python3 online submissions for Maximum Score of a Good Subarray.
    """

    def maximumScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        left = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                left[stack.pop()] = i

            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i

            stack.append(i)

        ans = 0
        for i in range(n):
            if left[i] < k and right[i] > k:
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))

        return ans


class Solution3:
    """
    leetcode solution 3: greedy
    Time: O(n)
    Space: O(1)
    Runtime: 1023 ms, faster than 70.92% of Python3 online submissions for Maximum Score of a Good Subarray.
    Memory Usage: 26.6 MB, less than 98.98% of Python3 online submissions for Maximum Score of a Good Subarray.
    """

    def maximumScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        left = k
        right = k
        ans = nums[k]
        curr_min = nums[k]

        while left > 0 or right < n - 1:
            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < n - 1 else 0):
                right += 1
                curr_min = min(curr_min, nums[right])
            else:
                left -= 1
                curr_min = min(curr_min, nums[left])

            ans = max(ans, curr_min * (right - left + 1))

        return ans
