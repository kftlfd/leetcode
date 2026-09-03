"""
Leetcode
2026-09-03
3876. Construct Uniform Parity Array II
Medium

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

    nums2[i] = nums1[i]
    nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1

Return true if it is possible to construct such an array, otherwise return false.

 

Example 1:

Input: nums1 = [1,4,7]

Output: true

Explanation:

    Set nums2[0] = nums1[0] = 1.
    Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
    Set nums2[2] = nums1[2] = 7.
    nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.

Example 2:

Input: nums1 = [2,3]

Output: false

Explanation:

It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.

Example 3:

Input: nums1 = [4,6]

Output: true

Explanation:

    Set nums2[0] = nums1[0] = 4.
    Set nums2[1] = nums1[1] = 6.
    nums2 = [4, 6], and all elements are even. Thus, the answer is true.

 

Constraints:

    1 <= n == nums1.length <= 10^5
    1 <= nums1[i] <= 10^9
    nums1 consists of distinct integers.


"""


class Solution01:
    """
    Runtime 72ms Beats 50.61%
    Memory 35.20MB Beats 85.98%
    """

    def uniformArray(self, nums1: list[int]) -> bool:
        min_even = None
        min_odd = None

        for num in nums1:
            if num % 2 == 0:
                if min_even is None:
                    min_even = num
                else:
                    min_even = min(min_even, num)
            else:
                if min_odd is None:
                    min_odd = num
                else:
                    min_odd = min(min_odd, num)

        return min_even is None or min_odd is None or min_odd < min_even


class Solution02:
    """
    Runtime 127ms Beats 18.29%
    Memory 41.31MB Beats 6.71%
    """

    def uniformArray(self, nums1: list[int]) -> bool:
        nums = set(nums1)
        evens = set(num for num in nums if num & 1 == 0)

        if len(evens) == 0 or len(evens) == len(nums):
            return True

        odds = nums - evens

        return min(evens) > min(odds)


class Solution1:
    """
    leetcode solution
    Runtime 29ms Beats 74.39%
    Memory 35.05MB Beats 93.90%
    """

    def uniformArray(self, nums1: list[int]) -> bool:
        mn = nums1[0]
        hasOdd = False
        for v in nums1:
            if v < mn:
                mn = v
            if v & 1:
                hasOdd = True
        if mn & 1:
            return True
        return not hasOdd


class Solution03:
    """
    Runtime 5ms Beats 99.39%
    Memory 35.20MB Beats 85.98%
    """

    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) & 1 == 1 or all(num & 1 == 0 for num in nums1)
