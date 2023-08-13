"""
Leetcode
2369. Check if There is a Valid Partition For The Array (medium)
2023-08-13

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

    The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
    The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
    The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.

Return true if the array has at least one valid partition. Otherwise, return false.

Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.

Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.

Constraints:

    2 <= nums.length <= 105
    1 <= nums[i] <= 106
"""

from typing import List


class Solution:
    """
    Runtime: 753 ms, faster than 100.00% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    Memory Usage: 30.4 MB, less than 68.46% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    """

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        # add [True, False] to the end to make dp[i+2] True and dp[i+3] False
        # for the first loop iteration
        dp = [False] * n + [True, False]

        # start from second to last num
        for i in range(n - 2, -1, -1):
            # case 1: nums[i:i+1] of 2 equal elemets
            if dp[i+2] and nums[i] == nums[i+1]:
                dp[i] = True
                continue

            # case 2: nums[i:i+2] of 3 equal elements, and
            # case 3: nums[i:i+2] of increasing elements
            if dp[i+3] and ((nums[i] == nums[i+1] and nums[i] == nums[i+2]) or
                            (nums[i] + 1 == nums[i+1] and nums[i] + 2 == nums[i+2])):
                dp[i] = True

        return dp[0]


class Solution1:
    """
    leetcode solution 1: top-down dp
    Time: O(n)
    Space: O(n)
    Runtime: 813 ms, faster than 97.69% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    Memory Usage: 92.4 MB, less than 38.46% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    """

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {-1: True}

        # Determine if the prefix array nums[0 ~ i] has a valid partition
        def prefixIsValid(i):
            if i in memo:
                return memo[i]

            ans = False

            if i > 0 and nums[i] == nums[i - 1]:
                ans |= prefixIsValid(i - 2)
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= prefixIsValid(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= prefixIsValid(i - 3)

            memo[i] = ans
            return ans

        return prefixIsValid(n - 1)


class Solution2:
    """
    leetcode solution 2: bottom-up dp
    Time: O(n)
    Space: O(n)
    Runtime: 936 ms, faster than 80.00% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    Memory Usage: 31.6 MB, less than 59.23% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    """

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n

        # Determine if the prefix array nums[0 ~ i] has a valid partition
        for i in range(n):
            dp_index = i + 1

            if i > 0 and nums[i] == nums[i - 1]:
                dp[dp_index] |= dp[dp_index - 2]

            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                dp[dp_index] |= dp[dp_index - 3]

            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                dp[dp_index] |= dp[dp_index - 3]

        return dp[n]


class Solution3:
    """
    leetcode solution 3: bottom-up dp space optimized
    Time: O(n)
    Space: O(1)
    Runtime: 935 ms, faster than 80.00% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    Memory Usage: 30.4 MB, less than 68.46% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    """

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        # only record the most recent 3 indices
        dp = [True] + [False] * 2

        # Determine if the prefix array nums[0 ~ i] has a valid partition
        for i in range(n):
            dp_index = i + 1
            ans = False

            if i > 0 and nums[i] == nums[i - 1]:
                ans |= dp[(dp_index - 2) % 3]

            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= dp[(dp_index - 3) % 3]

            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= dp[(dp_index - 3) % 3]

            dp[dp_index % 3] = ans

        return dp[n % 3]


s = Solution()
tests = [
    ([4, 4, 4, 5, 6],
     True),

    ([1, 1, 1, 2],
     False),
]
for inp, exp in tests:
    res = s.validPartition(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
