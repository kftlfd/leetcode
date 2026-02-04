"""
Leetcode
2026-02-04
3640. Trionic Array II
Hard

You are given an integer array nums of length n.

A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

    nums[l...p] is strictly increasing,
    nums[p...q] is strictly decreasing,
    nums[q...r] is strictly increasing.

Return the maximum sum of any trionic subarray in nums.

 

Example 1:

Input: nums = [0,-2,-1,-3,0,2,-1]

Output: -4

Explanation:

Pick l = 1, p = 2, q = 3, r = 5:

    nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
    nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
    nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
    Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.

Example 2:

Input: nums = [1,4,2,7]

Output: 14

Explanation:

Pick l = 0, p = 1, q = 2, r = 3:

    nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
    nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
    nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
    Sum = 1 + 4 + 2 + 7 = 14.

 

Constraints:

    4 <= n = nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    It is guaranteed that at least one trionic subarray exists.

 
Hint 1
Use dynamic programming
Hint 2
Let four arrays dp0...dp3 where dpk[i] is the max sum of a subarray ending at i after finishing k of the four phases (start -> inc -> dec -> inc)
Hint 3
Process each i>0
Hint 4
If nums[i] > nums[i-1], set dp1[i]=max(dp1[i-1]+nums[i], dp0[i-1]+nums[i]), dp3[i]=max(dp3[i-1]+nums[i], dp2[i-1]+nums[i])
Hint 5
If nums[i] < nums[i-1], set dp2[i]=max(dp2[i-1]+nums[i], dp1[i-1]+nums[i])
Hint 6
Always carry over dp0[i]=dp0[i-1]+nums[i] when nums[i]>nums[i-1]
Hint 7
Return the maximum value in dp3
"""

from typing import List


class Solution:
    """
    leetcode solution: Grouped Loop
    Runtime 158ms Beats 99.74%
    Memory 31.26MB Beats 99.35%
    """

    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        i = 0

        while i < n:
            j = i + 1
            res = 0

            # first segment: increasing segment
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1

            if p == i:  # 没有有效的increasing segment
                i += 1
                continue

            # second segment: decreasing segment
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1

            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue

            # third segment: increasing segment
            res += nums[q + 1]

            # find the maximum sum of the third segment
            max_sum = 0
            curr_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
                k += 1
            res += max_sum

            # find the maximum sum of the first segment
            max_sum = 0
            curr_sum = 0
            for k in range(p - 2, i - 1, -1):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
            res += max_sum

            # update answer
            ans = max(ans, res)
            i = q

        return int(ans)
