"""
Leetcode
2025-12-09
3583. Count Special Triplets
Medium

You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

    0 <= i < j < k < n, where n = nums.length
    nums[i] == nums[j] * 2
    nums[k] == nums[j] * 2

Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 1, 2), where:

    nums[0] = 6, nums[1] = 3, nums[2] = 6
    nums[0] = nums[1] * 2 = 3 * 2 = 6
    nums[2] = nums[1] * 2 = 3 * 2 = 6

Example 2:

Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 2, 3), where:

    nums[0] = 0, nums[2] = 0, nums[3] = 0
    nums[0] = nums[2] * 2 = 0 * 2 = 0
    nums[3] = nums[2] * 2 = 0 * 2 = 0

Example 3:

Input: nums = [8,4,2,8,4]

Output: 2

Explanation:

There are exactly two special triplets:

    (i, j, k) = (0, 1, 3)
        nums[0] = 8, nums[1] = 4, nums[3] = 8
        nums[0] = nums[1] * 2 = 4 * 2 = 8
        nums[3] = nums[1] * 2 = 4 * 2 = 8
    (i, j, k) = (1, 2, 4)
        nums[1] = 4, nums[2] = 2, nums[4] = 4
        nums[1] = nums[2] * 2 = 2 * 2 = 4
        nums[4] = nums[2] * 2 = 2 * 2 = 4

 

Constraints:

    3 <= n == nums.length <= 10^5
    0 <= nums[i] <= 10^5


Hint 1
Use frequency arrays or maps, e.g. freqPrev and freqNext—to track how many times each value appears before and after the current index.
Hint 2
For each index j in the triplet (i,j,k), compute its contribution to the answer using your freqPrev and freqNext counts.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 736ms Beats 60.36%
    Memory 45.90MB Beats 30.18%
    """

    def specialTriplets(self, nums: List[int]) -> int:
        freqPrev = defaultdict(int)
        freqNext = defaultdict(int)

        for i in range(len(nums) - 1, 0, -1):
            freqNext[nums[i]] += 1

        freqPrev[nums[0]] += 1

        ans = 0

        for i in range(1, len(nums) - 1):
            cur = nums[i]
            pair = cur * 2
            freqNext[cur] -= 1

            ans += freqPrev[pair] * freqNext[pair]

            freqPrev[cur] += 1

        return ans % (10**9 + 7)


class Solution1:
    """
    leetcode solution 1: Enumeration + Counting
    Runtime 496ms Beats 90.54%
    Memory 41.49MB Beats 69.82%
    """

    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        num_cnt = {}
        num_partial_cnt = {}

        for v in nums:
            num_cnt[v] = num_cnt.get(v, 0) + 1

        ans = 0
        for v in nums:
            target = v * 2
            l_cnt = num_partial_cnt.get(target, 0)
            num_partial_cnt[v] = num_partial_cnt.get(v, 0) + 1
            r_cnt = num_cnt.get(target, 0) - num_partial_cnt.get(target, 0)
            ans = (ans + l_cnt * r_cnt) % MOD

        return ans


class Solution2:
    """
    leetcode solution 2: Enumeration + Binary Search
    Runtime 769ms Beats 50.45%
    Memory 47.41MB Beats 17.11%
    """

    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        pos = defaultdict(list)

        for i, v in enumerate(nums):
            pos[v].append(i)

        def upper_bound(arr, i):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + ((r - l + 1) >> 1)
                if i >= arr[mid]:
                    l = mid
                else:
                    r = mid - 1
            return l + 1, len(arr) - 1 - l

        ans = 0
        for i in range(1, len(nums) - 1):
            target = nums[i] * 2
            if target in pos and len(pos[target]) > 1 and pos[target][0] < i:
                l, r = upper_bound(pos[target], i)
                if nums[i] == 0:
                    l -= 1
                ans = (ans + l * r) % MOD

        return ans
