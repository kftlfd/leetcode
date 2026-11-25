"""
Leetcode
2026-11-25
3934. Smallest Unique Subarray
Hard

You are given an integer array nums.

Find the minimum length of a subarray that is not identical to any other subarray in nums.

Return an integer denoting the minimum possible length of such a subarray.

Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.

 

Example 1:

Input: nums = [3,3,3]

Output: 3

Explanation:

    Subarrays of length 1: [3] → appears 3 times
    Subarrays of length 2: [3, 3] → appears 2 times
    Subarrays of length 3: [3, 3, 3] → appears once

The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.

Example 2:

Input: nums = [2,1,2,3,3]

Output: 1

Explanation:

Subarrays of length 1:

    [2] → appears 2 times
    [1] → appears once
    [3] → appears 2 times

The subarray [1] is unique, so the smallest unique subarray length is 1.

Example 3:

Input: nums = [1,1,2,2,1]

Output: 2

Explanation:

Subarrays of length 1:

    [1] → appears 3 times
    [2] → appears 2 times

Subarrays of length 2:

    [1, 1] → appears once
    [1, 2] → appears once
    [2, 2] → appears once
    [2, 1] → appears once

There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5


Hint 1
Think in terms of checking a fixed length len: count all subarrays of length len, and see whether any one appears exactly once.
Hint 2
Use rolling hash so each subarray can be represented in O(1) after preprocessing, instead of comparing arrays directly.
Hint 3
The answer can be binary searched because if there is a unique subarray of length len, then there is also a unique subarray of some length > len.
Hint 4
For each checked length, store frequencies of hashes in a hashmap. If any hash has frequency 1, that length works.
"""


class Solution1:
    """
    leetcode solution 1: Binary Search on the Answer + Rolling Hash
    Runtime 1142ms Beats 85.45%
    Memory 45.36MB Beats 60.00%
    """

    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        MOD = 1000000007
        BASE = 911382323

        n = len(nums)
        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1

        # Compute prefix hashes and powers of BASE
        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            p[i + 1] = p[i] * BASE % MOD

        def check(length):
            cnt = {}
            for l in range(n - length + 1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                cnt[key] = cnt.get(key, 0) + 1

            for times in cnt.values():
                if times == 1:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


class Solution2:
    """
    leetcode solution 2: Suffix Array
    Runtime 4902ms Beats 5.45%
    Memory 57.24MB Beats 29.09%
    """

    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Initial ranks
        rank = sorted(set(nums))
        comp = {v: i for i, v in enumerate(rank)}
        rank = [comp[x] for x in nums]

        sa = list(range(n))
        k = 1
        tmp = [0] * n

        while k < n:
            # One sort suffices (tuple comparison handles both keys)
            sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))

            tmp[sa[0]] = 0
            prev = sa[0]
            for idx in range(1, n):
                cur = sa[idx]
                a1 = rank[prev]
                a2 = rank[prev + k] if prev + k < n else -1
                b1 = rank[cur]
                b2 = rank[cur + k] if cur + k < n else -1
                tmp[cur] = tmp[prev] + (0 if (a1 == b1 and a2 == b2) else 1)
                prev = cur

            rank, tmp = tmp, rank
            if rank[sa[-1]] == n - 1:
                break
            k <<= 1

        # Kasai LCP
        pos = [0] * n
        for i in range(n):
            pos[sa[i]] = i

        lcp = [0] * n
        h = 0
        for i in range(n):
            pi = pos[i]
            if pi == 0:
                h = 0
                continue
            j = sa[pi - 1]
            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1
            lcp[pi] = h
            if h:
                h -= 1

        answer = n
        for i in range(n):
            nxt = lcp[i + 1] if i + 1 < n else 0
            need = (lcp[i] if lcp[i] > nxt else nxt) + 1
            if sa[i] + need - 1 < n and need < answer:
                answer = need

        return answer
