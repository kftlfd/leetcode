"""
Leetcode
2025-04-16
2537. Count the Number of Good Subarrays
Medium

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.



Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i], k <= 10^9


Hint 1
For a fixed index l, try to find the minimum value of index r, such that the subarray is not good
Hint 2
When a number is added to a subarray, it increases the number of pairs by its previous appearances.
Hint 3
When a number is removed from the subarray, it decreases the number of pairs by its remaining appearances.
Hint 4
Maintain 2-pointers l and r such that we can keep in account the number of equal pairs.
"""

from collections import Counter
from typing import List


class Solution:
    """
    leetcode solution 1: Two pointers
    Runtime 206ms Beats 12.62%
    Memory 34.46MB Beats 45.31%
    """

    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
            if same >= k:
                ans += n - right
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
        return ans
