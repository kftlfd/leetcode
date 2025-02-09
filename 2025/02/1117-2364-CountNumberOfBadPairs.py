"""
Leetcode
2025-02-09
2364. Count Number of Bad Pairs
Medium
Topics
Companies
Hint

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9


Hint 1
Would it be easier to count the number of pairs that are not bad pairs?
Hint 2
Notice that (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j).
Hint 3
Keep a counter of nums[i] - i. To be efficient, use a HashMap.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime 109ms Beats 19.05%
    Memory 38.89MB Beats 59.29%
    """

    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n * (n - 1) // 2  # total pairs

        cnt = Counter()
        for i, num in enumerate(nums):
            cnt[num - i] += 1

        for count in cnt.values():
            if count > 1:
                ans -= count * (count - 1) // 2  # pairs with the same delta

        return ans


class Solution1:
    """
    leetcode solution: Hash Map
    Runtime 61ms Beats 91.90%
    Memory 38.86MB Beats 59.29%
    """

    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        diff_count = {}

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            # Count of previous positions with same difference
            good_pairs_count = diff_count.get(diff, 0)

            # Total possible pairs minus good pairs = bad pairs
            bad_pairs += pos - good_pairs_count

            # Update count of positions with this difference
            diff_count[diff] = good_pairs_count + 1

        return bad_pairs
