"""
Leetcode
2026-10-20
3886. Sum of Sortable Integers
Hard

You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

    Partition nums into consecutive subarrays of length k.
    Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers k.

 

Example 1:

Input: nums = [3,1,2]

Output: 3

Explanation:

    For n = 3, possible divisors are 1 and 3.
    For k = 1: each subarray has one element. No rotation can sort the array.
    For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
    Only k = 3 is sortable. Hence, the answer is 3.

Example 2:

Input: nums = [7,6,5]

Output: 0

Explanation:

    For n = 3, possible divisors are 1 and 3.
    For k = 1: each subarray has one element. No rotation can sort the array.
    For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
    No k is sortable. Hence, the answer is 0.

Example 3:

Input: nums = [5,8]

Output: 3

Explanation:

    For n = 2, possible divisors are 1 and 2.
    Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

 

Constraints:

    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= 10^5


Hint 1
First, observe that k must divide n, since the array is partitioned into subarrays of length k. Iterate over all divisors of n.
Hint 2
Let s be the sorted version of the array. For each divisor k, check every block [i, i+k).
Hint 3
A block can be rotated to match its sorted counterpart if the sorted segment s[i..i+k-1] appears as a cyclic rotation of nums[i..i+k-1].
Hint 4
You can test this by checking whether the sorted segment exists inside two concatenated copies of the block. If all blocks satisfy this, then k is sortable.
"""


from math import isqrt


class Solution:
    """
    Time Limit Exceeded
    """

    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divs = self._get_divisors(n)

        if nums == sorted(nums):
            return sum(divs)

        return sum(k for k in divs
                   if k != 1 and self._is_sortable_int(k, nums))

    def _get_divisors(self, n: int) -> list[int]:
        divisors = [1]
        if n < 2:
            return divisors
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                divisors.append(i)
        divisors.append(n)
        return divisors

    def _is_sortable_int(self, k: int, nums: list[int]) -> bool:
        prev = 0
        for i in range(0, len(nums), k):
            block = nums[i:i+k]
            sblock = sorted(block)
            if not self._can_rotate_to_match(block, sblock) or sblock[0] < prev:
                return False
            prev = sblock[-1]
        return True

    def _can_rotate_to_match(self, nums: list[int], target: list[int]) -> bool:
        n = len(nums)
        numsnums = nums + nums
        for i in range(n):
            if numsnums[i:i+n] == target:
                return True
        return False


class Solution1:
    """
    leetcode solution 1: KMP
    Runtime 3638ms Beats 15.38%
    Memory 32.38MB Beats 42.86%
    """

    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        fac = []
        for x in range(1, isqrt(n) + 1):
            if n % x == 0:
                fac.append(x)
                if n // x != x:
                    fac.append(n // x)

        target = sorted(nums)

        def kmp(nums1, nums2):
            n, m = len(nums1), len(nums2)

            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and nums2[i] != nums2[j]:
                    j = pi[j - 1]

                if nums2[i] == nums2[j]:
                    j += 1

                pi[i] = j

            j = 0
            for i in range(n):
                while j > 0 and nums1[i] != nums2[j]:
                    j = pi[j - 1]

                if nums1[i] == nums2[j]:
                    j += 1

                if j == m:
                    return True

            return False

        def check(nums1, nums2):
            # Check whether cyclic rotations of nums1 can produce nums2
            return kmp(nums1 + nums1, nums2)

        ans = 0

        for d in fac:
            for left in range(0, n, d):
                right = left + d - 1

                if not check(nums[left: right + 1], target[left: right + 1]):
                    break
            else:
                ans += d

        return ans


class Solution2:
    """
    leetcode solution 2: Case Analysis
    Runtime 1156ms Beats 79.12%
    Memory 31.33MB Beats 69.23%
    """

    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        fac = []
        for x in range(1, isqrt(n) + 1):
            if n % x == 0:
                fac.append(x)
                if n // x != x:
                    fac.append(n // x)

        target = sorted(nums)

        def check(nums1, nums2):
            # Check whether cyclic rotations of nums1 can produce nums2
            L = len(nums1)

            for i in range(L - 1):
                if nums1[i] > nums1[i + 1]:
                    return nums1[i + 1:] + nums1[: i + 1] == nums2

            return nums1 == nums2

        ans = 0

        for d in fac:
            for left in range(0, n, d):
                right = left + d - 1

                if not check(nums[left: right + 1], target[left: right + 1]):
                    break
            else:
                ans += d

        return ans


s = Solution()
tests = [
    ([3, 1, 2],
     3),
]
for inp, exp in tests:
    res = s.sortableIntegers(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
