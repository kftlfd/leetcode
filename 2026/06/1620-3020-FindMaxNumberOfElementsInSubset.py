"""
Leetcode
2026-06-27
3020. Find the Maximum Number of Elements in Subset
Medium

You are given an array of positive integers nums.

You need to select a of nums which satisfies the following condition:

    You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] (Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.

Return the maximum number of elements in a subset that satisfies these conditions.

 

Example 1:

Input: nums = [5,4,1,2,2]
Output: 3
Explanation: We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 22 == 4. Hence the answer is 3.

Example 2:

Input: nums = [1,3,2,4]
Output: 1
Explanation: We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {3}, or {4}, there may be multiple subsets which provide the same answer. 

 

Constraints:

    2 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9


Hint 1
We can select an odd number of 1's.
Hint 2
Put all the values into a HashSet. We can start from each x > 1 as the smallest chosen value and we can find the longest subset by checking the new values (which are the square of the previous value) in the set by brute force.
Hint 3
Note when x > 1, x2, x4, x8, … increases very fast, the longest subset with smallest value x cannot be very long. (The length is O(log(log(109))).
Hint 4
Hence we can directly check all lengths less than 10 for all values of x.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime 112ms Beats 68.50%
    Memory 31.71MB Beats 49.61%
    """

    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = cnt[1]
        if ans > 1 and ans % 2 == 0:
            ans -= 1

        for num in cnt:
            if num == 1:
                continue
            val = num
            nxt_power = 2
            seq_len = 0
            cont = True
            while cont:
                cont = False
                cur = cnt[val]
                if cur > 1:
                    seq_len += 2
                    cont = True
                elif cur == 1:
                    seq_len += 1
                    break
                else:
                    break
                val = pow(num, nxt_power)
                nxt_power *= 2
            if seq_len > 1 and seq_len % 2 == 0:
                seq_len -= 1
            ans = max(ans, seq_len)

        return ans


class Solution1:
    """
    leetcode solution: Hash Table + Enumeration
    Runtime 91ms Beats 94.49%
    Memory 31.98MB Beats 25.98%
    """

    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        one_cnt = cnt.get(1, 0)

        # ans is at least the number of occurrences of 1, rounded down to an odd number
        ans = one_cnt if one_cnt % 2 else one_cnt - 1

        cnt.pop(1, None)

        for num in cnt:
            res = 0
            x = num
            while x in cnt and cnt[x] > 1:
                res += 2
                x *= x
            ans = max(ans, res + (1 if x in cnt else -1))

        return ans
