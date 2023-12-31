"""
Leetcode
2616. Minimize the Maximum Difference of Pairs (medium)
2023-08-09

You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= p <= (nums.length)/2
"""

from typing import List


class Solution:
    """
    leetcode solution: greedy + binary search
    Time: O(n * log(V)) -- n = len(nums), V = max(nums)
    Space: O(1)
    Runtime: 976 ms, faster than 87.74% of Python3 online submissions for Minimize the Maximum Difference of Pairs.
    Memory Usage: 30.9 MB, less than 96.13% of Python3 online submissions for Minimize the Maximum Difference of Pairs.
    """

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        def count_valid_pairs(max_allowed_diff: int) -> int:
            index = 0
            count = 0
            while index < n - 1:
                # If valid pair is fount, skip both numbers
                if nums[index + 1] - nums[index] <= max_allowed_diff:
                    count += 1
                    index += 1
                index += 1
            return count

        left = 0
        right = nums[-1] - nums[0]  # max diff in array
        while left < right:
            mid = left + (right - left) // 2
            # if there are enough pairs, look for a smaller max_diff
            # otherwise, look for a larger max_diff
            if count_valid_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
tests = [
    (([10, 1, 2, 7, 1, 3], 2),
     1),

    (([4, 2, 1, 2], 1),
     0),
]
for inp, exp in tests:
    res = s.minimizeMax(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
