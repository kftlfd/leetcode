"""
Leetcode
2026-06-10
3691. Maximum Total Subarray Value II
Hard

You are given an integer array nums of length n and an integer k.

You must select exactly k distinct nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.

The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.

 

Example 1:

Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

    Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
    Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.

Adding these gives 2 + 2 = 4.

Example 2:

Input: nums = [4,2,5,1], k = 3

Output: 12

Explanation:

One optimal approach is:

    Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
    Choose nums[1..3] = [2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
    Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.

Adding these gives 4 + 4 + 4 = 12.

 

Constraints:

    1 <= n == nums.length <= 5 * 10^4
    0 <= nums[i] <= 10^9
    1 <= k <= min(10^5, n * (n + 1) / 2)


Hint 1
For fixed l, the sequence v(l,r)=max(nums[l..r])−min(nums[l..r]) is non-increasing as r moves left.
Hint 2
Build RMQs (sparse tables) for range max/min so each v(l,r) is queryable in O(1).
Hint 3
Use a max-heap with v(l,n-1) for all l; pop the largest k times, and after popping an entry from (l,r) push (l,r-1) if r>l.
"""

import heapq
from typing import List


class Solution1:
    """
    leetcode solution 1: Sparse Table + Max Heap
    Runtime 3236ms Beats 68.29%
    Memory 51.70MB Beats 53.66%
    """

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        logn = n.bit_length()
        stMax = [[0] * logn for _ in range(n)]
        stMin = [[0] * logn for _ in range(n)]
        for i in range(n):
            stMax[i][0] = stMin[i][0] = nums[i]
        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                stMax[i][j] = max(stMax[i][j - 1], stMax[i + step][j - 1])
                stMin[i][j] = min(stMin[i][j - 1], stMin[i + step][j - 1])

        def queryMax(l: int, r: int) -> int:
            j = (r - l + 1).bit_length() - 1
            return max(stMax[l][j], stMax[r - (1 << j) + 1][j])

        def queryMin(l: int, r: int) -> int:
            j = (r - l + 1).bit_length() - 1
            return min(stMin[l][j], stMin[r - (1 << j) + 1][j])

        pq = [
            (-(queryMax(l, n - 1) - queryMin(l, n - 1)), l, n - 1)
            for l in range(n)
        ]
        heapq.heapify(pq)
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            if r > l:
                heapq.heappush(
                    pq, (-(queryMax(l, r - 1) - queryMin(l, r - 1)), l, r - 1)
                )
        return ans


class Solution2:
    """
    leetcode solution 2: Segment Tree + Max Heap
    Runtime 9545ms Beats 17.07%
    Memory 34.58MB Beats 78.05%
    """

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = self.SegTree(nums)
        pq = [
            (
                -(
                    seg.queryMax(1, 0, n - 1, l, n - 1)
                    - seg.queryMin(1, 0, n - 1, l, n - 1)
                ),
                l,
                n - 1,
            )
            for l in range(n)
        ]
        heapq.heapify(pq)
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            if r > l:
                heapq.heappush(
                    pq,
                    (
                        -(
                            seg.queryMax(1, 0, n - 1, l, r - 1)
                            - seg.queryMin(1, 0, n - 1, l, r - 1)
                        ),
                        l,
                        r - 1,
                    ),
                )
        return ans

    class SegTree:
        def __init__(self, nums: List[int]):
            self.n = len(nums)
            self.maxv = [0] * (4 * self.n)
            self.minv = [0] * (4 * self.n)
            self.build(1, 0, self.n - 1, nums)

        def build(self, node: int, l: int, r: int, nums: List[int]):
            if l == r:
                self.maxv[node] = self.minv[node] = nums[l]
                return
            m = (l + r) // 2
            self.build(node * 2, l, m, nums)
            self.build(node * 2 + 1, m + 1, r, nums)
            self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])
            self.minv[node] = min(self.minv[node * 2], self.minv[node * 2 + 1])

        def queryMax(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
            if ql <= l and r <= qr:
                return self.maxv[node]
            m = (l + r) // 2
            res = -(10**18)
            if ql <= m:
                res = max(res, self.queryMax(node * 2, l, m, ql, qr))
            if qr > m:
                res = max(res, self.queryMax(node * 2 + 1, m + 1, r, ql, qr))
            return res

        def queryMin(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
            if ql <= l and r <= qr:
                return self.minv[node]
            m = (l + r) // 2
            res = 10**18
            if ql <= m:
                res = min(res, self.queryMin(node * 2, l, m, ql, qr))
            if qr > m:
                res = min(res, self.queryMin(node * 2 + 1, m + 1, r, ql, qr))
            return res
