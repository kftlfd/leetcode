"""
Leetcode
2026-09-22
3525. Find X Value of Array II
Hard

You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

For each query in queries you need to determine the x-value of nums for xi after performing the following actions:

    Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
    Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).

Return an array result of size queries.length where result[i] is the answer for the ith query.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Note that x-value has a different definition in this version.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

Output: [2,2,2]

Explanation:

    For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
        Remove the suffix [2, 4, 5]. nums becomes [1, 2].
        Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
    For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
        Remove the empty suffix. nums becomes [3, 5].
        Remove the suffix [5]. nums becomes [3].
    For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
        Remove the suffix [2, 2, 3, 5]. nums becomes [1].
        Remove the suffix [3, 5]. nums becomes [1, 2, 2].

Example 2:

Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

Output: [1,0]

Explanation:

    For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
        Remove the suffix [2, 4, 8, 16, 32].
    For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.

Example 3:

Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

Output: [5]

 

Constraints:

    1 <= nums[i] <= 10^9
    1 <= nums.length <= 10^5
    1 <= k <= 5
    1 <= queries.length <= 2 * 10^4
    queries[i] == [indexi, valuei, starti, xi]
    0 <= indexi <= nums.length - 1
    1 <= valuei <= 10^9
    0 <= starti <= nums.length - 1
    0 <= xi <= k - 1


Hint 1
Use a segment tree to efficiently maintain and merge product prefix information for the array nums.
Hint 2
In each segment tree node, store a frequency count of prefix product remainders for every x in the range [0, k - 1].
Hint 3
For each query, update nums[index] to value, then merge the segments corresponding to nums[start..n - 1] to compute the x-value for xi.
"""

from typing import List


class Solution:
    """
    leetcode solution: Segment Tree
    Runtime 5047ms Beats 50.98%
    Memory 64.70MB Beats 72.55%
    """

    class SegmentTree:
        def __init__(self, nums: List[int], k: int):
            self.k = k
            n = len(nums)
            size = 2 << n.bit_length()

            # tree[o] = pre + [mul]
            self.tree = [[0] * (k + 1) for _ in range(size)]

            self.build(nums, 1, 0, n - 1)

        def makeLeaf(self, o: int, value: int) -> None:
            info = [0] * (self.k + 1)
            r = value % self.k
            info[r] = 1
            info[self.k] = r  # mul
            self.tree[o] = info

        def mergePre(self, left: List[int], right: List[int]) -> List[int]:
            pre = [0] * (self.k + 1)

            mul_L = left[self.k]
            mul_R = right[self.k]

            # Remainder of the product of the entire interval
            pre[self.k] = (mul_L * mul_R) % self.k

            # Case 1: Entirely within the left interval
            for x in range(self.k):
                pre[x] = left[x]

            # Case 2: Contains the entire left interval, followed by a prefix of the right interval
            for x in range(self.k):
                pre[(mul_L * x) % self.k] += right[x]

            return pre

        def maintain(self, o: int) -> None:
            self.tree[o] = self.mergePre(
                self.tree[o * 2],
                self.tree[o * 2 + 1],
            )

        def build(self, nums: List[int], o: int, l: int, r: int) -> None:
            if l == r:
                self.makeLeaf(o, nums[l])
                return

            m = (l + r) // 2
            self.build(nums, o * 2, l, m)
            self.build(nums, o * 2 + 1, m + 1, r)
            self.maintain(o)

        def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
            if l == r:
                self.makeLeaf(o, value)
                return

            m = (l + r) // 2
            if index <= m:
                self.update(o * 2, l, m, index, value)
            else:
                self.update(o * 2 + 1, m + 1, r, index, value)

            self.maintain(o)

        def query(self, o: int, l: int, r: int, L: int, R: int) -> List[int]:
            if L <= l and r <= R:
                return self.tree[o]

            m = (l + r) // 2
            if R <= m:
                return self.query(o * 2, l, m, L, R)
            if L > m:
                return self.query(o * 2 + 1, m + 1, r, L, R)

            left = self.query(o * 2, l, m, L, R)
            right = self.query(o * 2 + 1, m + 1, r, L, R)
            return self.mergePre(left, right)

    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = self.SegmentTree(nums, k)

        ans = []
        for index, value, start, x in queries:
            seg.update(1, 0, n - 1, index, value)
            pre = seg.query(1, 0, n - 1, start, n - 1)
            ans.append(pre[x])

        return ans
