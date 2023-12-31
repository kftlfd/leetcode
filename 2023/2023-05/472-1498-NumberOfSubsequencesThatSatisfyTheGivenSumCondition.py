"""
Leetcode
1498. Number of Subsequences That Satisfy the Given Sum Condition (medium)
2023-05-06

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
"""

from typing import List
from bisect import bisect_right


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime: 859 ms, faster than 62.44% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
    Memory Usage: 29.1 MB, less than 10.80% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
    """

    def numSubseq(self, nums: List[int], target: int) -> int:

        n = len(nums)
        mod = 10**9 + 7
        nums = sorted(nums)
        ans = 0

        for left in range(n):
            # Find the insertion position for `target - nums[left]`
            # 'right' equals the insertion index minus 1.
            right = bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                ans += pow(2, right - left, mod)

        return ans % mod


class Solution2:
    """
    leetcode solution 2: Two Pointers
    Runtime: 813 ms, faster than 81.03% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
    Memory Usage: 29.1 MB, less than 10.80% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
    """

    def numSubseq(self, nums: List[int], target: int) -> int:

        n = len(nums)
        mod = 10**9 + 7
        nums = sorted(nums)
        ans = 0

        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1

        return ans


s = Solution2()
tests = [
    (([3, 5, 6, 7], 9),
     4),

    (([3, 3, 6, 8], 10),
     6),

    (([2, 3, 3, 4, 6, 7], 12),
     61),
]
for inp, exp in tests:
    res = s.numSubseq(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
