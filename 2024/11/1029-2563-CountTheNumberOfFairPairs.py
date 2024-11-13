"""
Leetcode
2024-11-13
2563. Count the Number of Fair Pairs
Medium

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper

 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

 

Constraints:

    1 <= nums.length <= 10^5
    nums.length == n
    -10^9 <= nums[i] <= 10^9
    -10^9 <= lower <= upper <= 10^9
"""

from typing import List


class Solution:
    """
    Runtime: 728 ms, faster than 32.14% of Python3 online submissions for Count the Number of Fair Pairs.
    Memory Usage: 30.7 MB, less than 61.70% of Python3 online submissions for Count the Number of Fair Pairs.
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 0

        for i, num in enumerate(nums):
            min_to_pair = lower - num
            lo = i + 1
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < min_to_pair:
                    lo = mid + 1
                else:
                    hi = mid
            left_i = lo
            if left_i < i + 1 or left_i >= n or not lower <= num + nums[left_i] <= upper:
                continue

            max_to_pair = upper - num
            lo = i + 1
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= max_to_pair:
                    lo = mid + 1
                else:
                    hi = mid

            right_i = hi - 1
            if right_i < i + 1 or right_i >= n or not lower <= num + nums[right_i] <= upper:
                continue

            ans += right_i - left_i + 1

        return ans


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime: 1120 ms, faster than 14.29% of Python3 online submissions for Count the Number of Fair Pairs.
    Memory Usage: 30.7 MB, less than 61.70% of Python3 online submissions for Count the Number of Fair Pairs.
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        ans = 0
        for i, num in enumerate(nums):
            # Assume we have picked nums[i] as the first pair element.

            # `low` indicates the number of possible pairs with sum < lower.
            low = self.lower_bound(nums, i + 1, len(nums) - 1, lower - num)

            # `high` indicates the number of possible pairs with sum <= upper.
            high = self.lower_bound(
                nums, i + 1, len(nums) - 1, upper - num + 1)

            # Their difference gives the number of elements with sum in the
            # given range.
            ans += high - low

        return ans

    def lower_bound(self, nums, low, high, element):
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] >= element:
                high = mid - 1
            else:
                low = mid + 1
        return low


class Solution2:
    """
    leetcode solution 2: Two Pointers
    Runtime: 100 ms, faster than 98.21% of Python3 online submissions for Count the Number of Fair Pairs.
    Memory Usage: 30.5 MB, less than 97.40% of Python3 online submissions for Count the Number of Fair Pairs.
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    # Calculate the number of pairs with sum less than `value`.
    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            cur_sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the
            # next index.
            if cur_sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
        return result


s = Solution()
tests = [
    (([0, 0, 0, 0, 0, 0], 0, 0),
     15),

    (([0, 1, 7, 4, 4, 5], 3, 6),
     6),

    (([1, 7, 9, 2, 5], 11, 11),
     1),
]
for inp, exp in tests:
    res = s.countFairPairs(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
