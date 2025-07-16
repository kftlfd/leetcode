"""
Leetcode
2025-07-16
3201. Find the Maximum Length of Valid Subsequence I
Medium

You are given an integer array nums.

A subsequence sub of nums with length x is called valid if it satisfies:

    (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.

Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].

 

Constraints:

    2 <= nums.length <= 2 * 10^5
    1 <= nums[i] <= 10^7

    
Hint 1
The possible sequence either contains all even elements, all odd elements, alternate even odd, or alternate odd even elements.
Hint 2
Considering only the parity of elements, there are only 4 possibilities and we can try all of them.
Hint 3
When selecting an element with any parity, try to select the earliest one.
"""

from typing import List


class Solution:
    """
    Runtime 68ms Beats 58.14%
    Memory 38.96MB Beats 82.95%
    """

    def maximumLength(self, nums: List[int]) -> int:
        EVEN = 0
        ODD = 1

        all_odd = 0
        all_even = 0
        alt_odd = 0
        alt_even = 0

        alt_odd_next = ODD
        alt_even_next = EVEN

        for num in nums:
            parity = num & 1 == 1

            if parity == EVEN:
                all_even += 1
            else:
                all_odd += 1

            if alt_odd_next == parity:
                alt_odd += 1
                alt_odd_next ^= 1

            if alt_even_next == parity:
                alt_even += 1
                alt_even_next ^= 1

        return max(all_odd, all_even, alt_odd, alt_even)


class Solution1:
    """
    leetcode solution: Parity of Enumeration Elements
    Runtime 139ms Beats 19.38%
    Memory 39.01MB Beats 72.09%
    """

    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res
