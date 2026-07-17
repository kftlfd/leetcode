"""
Leetcode
2026-07-17
3312. Sorted GCD Pair Queries
Hard

You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.

 

Example 1:

Input: nums = [2,3,4], queries = [0,2,2]

Output: [1,2,2]

Explanation:

gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

After sorting in ascending order, gcdPairs = [1, 1, 2].

So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].

Example 2:

Input: nums = [4,4,2,1], queries = [5,3,1,0]

Output: [4,2,1,1]

Explanation:

gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].

Example 3:

Input: nums = [2,2], queries = [0,0]

Output: [2,2]

Explanation:

gcdPairs = [2].

 

Constraints:

    2 <= n == nums.length <= 10^5
    1 <= nums[i] <= 5 * 10^4
    1 <= queries.length <= 10^5
    0 <= queries[i] < n * (n - 1) / 2


Hint 1
Try counting the number of pairs that have a GCD of g
Hint 2
Use inclusion-exclusion.
"""

from bisect import bisect_left
from typing import List


class Solution:
    """
    leetcode solution: Inclusion-Exclusion Principle + Prefix Sum + Binary Search
    Runtime 535ms Beats 52.50%
    Memory 40.06MB Beats 62.50%
    """

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # The key observation is that although there are many pairs, the range
        # of possible GCD values is small: every GCD lies in the range [1,m],
        # where m <= 5*(10^4). Therefore, instead of enumerating pairs, we
        # enumerate all possible GCD values and count how many pairs have each
        # value as their GCD.
        m = max(nums)

        # First, count the occurrences of each value in nums and store them in the array cnt.
        cnt = [0] * (m + 1)
        for num in nums:
            cnt[num] += 1

        # Then, for every positive integer i∈[1,m], enumerate all of its multiples
        # to count how many elements in nums are divisible by i. Any pair formed
        # from these elements has a GCD of at least i.

        # However, "at least i" is not the same as "exactly i", because it also
        # includes pairs whose GCD is 2i, 3i, and so on. To obtain the number of
        # pairs whose GCD is exactly i, we traverse i from large to small and apply
        # the inclusion-exclusion principle. Specifically, we first count all pairs
        # whose GCD is at least i, then subtract the numbers of pairs whose GCD is
        # 2i, 3i, and so on. The remaining count is exactly the number of pairs
        # whose GCD equals i.

        # Finally, compute the prefix sum of these counts. The prefix sum at
        # index i represents the number of pairs whose GCD is at most i.

        for i in range(1, m + 1):
            for j in range(i * 2, m + 1, i):
                cnt[i] += cnt[j]
        for i in range(1, m + 1):
            cnt[i] = cnt[i] * (cnt[i] - 1) // 2
        for i in range(m, 0, -1):
            for j in range(i * 2, m + 1, i):
                cnt[i] -= cnt[j]
        for i in range(1, m + 1):
            cnt[i] += cnt[i - 1]

        # For each query queries[i], we perform a binary search on the prefix sum array
        # to find the smallest GCD value whose cumulative count exceeds the query.

        ans = []
        for q in queries:
            q += 1
            pos = bisect_left(cnt, q)
            ans.append(pos)

        return ans
