"""
Leetcode
2026-11-04
3505. Minimum Operations to Make Elements Within K Subarrays Equal
Hard

You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):

    Increase or decrease any element of nums by 1.

Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

 

Example 1:

Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

Output: 8

Explanation:

    Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
    Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
    Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

Example 2:

Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2

Output: 3

Explanation:

    Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
    Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

 

Constraints:

    2 <= nums.length <= 10^5
    -10^6 <= nums[i] <= 10^6
    2 <= x <= nums.length
    1 <= k <= 15
    2 <= k * x <= nums.length


Hint 1
Making every element of an x-sized window equal to its median is optimal.
Hint 2
Precalculate this for each window.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List

from sortedcontainers import SortedList


class Solution1:
    """
    leetcode solution 1: Sliding Window + Two Heaps + Mathematics + Dynamic Programming
    Runtime 2484ms Beats 77.61%
    Memory 63.32MB Beats 7.46%
    """

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left, right = [], []
        delayed = defaultdict(int)
        left_size = right_size = 0
        sum_l = sum_r = 0
        ops = [0] * n

        def prune(h: List[int], sign: int) -> None:
            while h and delayed[sign * h[0]]:
                delayed[sign * h[0]] -= 1
                heappop(h)

        def balance() -> None:
            nonlocal left_size, right_size, sum_l, sum_r
            if left_size > right_size + 1:
                num = -heappop(left)
                heappush(right, num)
                sum_r += num
                sum_l -= num
                right_size += 1
                left_size -= 1
                prune(left, -1)
            elif right_size > left_size:
                num = heappop(right)
                heappush(left, -num)
                sum_l += num
                sum_r -= num
                left_size += 1
                right_size -= 1
                prune(right, 1)

        for i, num in enumerate(nums):
            if not left or num <= -left[0]:
                heappush(left, -num)
                left_size += 1
                sum_l += num
            else:
                heappush(right, num)
                right_size += 1
                sum_r += num
            balance()
            if i >= x:
                num = nums[i - x]
                delayed[num] += 1
                if num <= -left[0]:
                    left_size -= 1
                    sum_l -= num
                    if num == -left[0]:
                        prune(left, -1)
                else:
                    right_size -= 1
                    sum_r -= num
                    if num == right[0]:
                        prune(right, 1)
                balance()
            if i >= x - 1:
                mid = -left[0]
                ops[i] = sum_r - sum_l + mid * (left_size - right_size)

        inf = 1 << 31
        dp = [[0] + [inf] * k for _ in range(n)]
        for j in range(1, k + 1):
            if j == 1:
                dp[x - 1][j] = ops[x - 1]
            else:
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + ops[j * x - 1]
        for j in range(1, k + 1):
            for i in range(j * x, n):
                dp[i][j] = min(dp[i - x][j - 1] + ops[i], dp[i - 1][j])
        return dp[n - 1][k]


class Solution2:
    """
    leetcode solution 2: Sliding Window + Ordered Multisets + Mathematics + Dynamic Programming (Rolling Arrays)
    Runtime 3591ms Beats 59.70%
    Memory 37.44MB Beats 95.52%
    """

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left, right = SortedList(), SortedList()
        sum_l = sum_r = 0
        ops = [0] * n

        for i, value in enumerate(nums):
            if not left or value <= left[-1]:
                left.add(value)
                sum_l += value
            else:
                right.add(value)
                sum_r += value
            if i >= x:
                value = nums[i - x]
                if value in left:
                    left.remove(value)
                    sum_l -= value
                else:
                    right.remove(value)
                    sum_r -= value
            if len(left) > len(right) + 1:
                value = left.pop()
                right.add(value)
                sum_l -= value
                sum_r += value
            elif len(left) < len(right):
                value = right.pop(0)
                left.add(value)
                sum_l += value
                sum_r -= value
            if i >= x - 1:
                mid = left[-1]
                ops[i] = mid * len(left) - sum_l + sum_r - mid * len(right)

        inf = 1 << 40
        pre = [0] * (n + 1)
        cur = [inf] * (n + 1)
        for j in range(1, k + 1):
            for i in range(n + 1):
                cur[i] = inf
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], pre[i - x] + ops[i - 1])
            pre, cur = cur, pre
        return pre[n]
