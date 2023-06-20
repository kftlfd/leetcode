"""
Leetcode
2090. K Radius Subarray Averages (medium)
2023-06-20

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

    For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Example 1:

Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.

Example 2:

Input: nums = [100000], k = 0
Output: [100000]
Explanation:
- The sum of the subarray centered at index 0 with radius 0 is: 100000.
  avg[0] = 100000 / 1 = 100000.

Example 3:

Input: nums = [8], k = 100000
Output: [-1]
Explanation: 
- avg[0] is -1 because there are less than k elements before and after index 0.

Constraints:

    n == nums.length
    1 <= n <= 10^5
    0 <= nums[i], k <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime: 1611 ms, faster than 83.99% of Python3 online submissions for K Radius Subarray Averages.
    Memory Usage: 34.5 MB, less than 77.68% of Python3 online submissions for K Radius Subarray Averages.
    """

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        window_len = k*2 + 1
        window_sum = sum(nums[:window_len])

        for i in range(k, len(nums) - k):
            ans[i] = window_sum // window_len
            window_sum -= nums[i - k]
            if i + k + 1 < len(nums):
                window_sum += nums[i + k + 1]

        return ans


class Solution1:
    """
    Runtime: 1567 ms, faster than 96.18% of Python3 online submissions for K Radius Subarray Averages.
    Memory Usage: 34.1 MB, less than 96.18% of Python3 online submissions for K Radius Subarray Averages.
    """

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        ans = [-1] * len(nums)
        window_len = k*2 + 1

        if window_len > len(nums):
            return ans

        window_sum = sum(nums[i] for i in range(window_len))
        ans[k] = window_sum // window_len

        for i in range(k + 1, len(nums) - k):
            window_sum += -nums[i - k - 1] + nums[i + k]
            ans[i] = window_sum // window_len

        return ans


class Solution2:
    """
    leetcode solution 1: Prefix Sum
    Runtime: 1614 ms, faster than 83.11% of Python3 online submissions for K Radius Subarray Averages.
    Memory Usage: 35.2 MB, less than 28.78% of Python3 online submissions for K Radius Subarray Averages.
    """

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # When a single element is considered then its averafge will be the number itself only.
        if k == 0:
            return nums

        n = len(nums)
        averages = [-1] * n

        # Any index will not have 'k' elements in it's left and right.
        if 2 * k + 1 > n:
            return averages

        # Generate 'prefix' array for 'nums'.
        # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # We iterate only on those indices which have atleast 'k' elements in their left and right.
        # i.e. indices from 'k' to 'n - k'
        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // (2 * k + 1)
            averages[i] = average

        return averages


s = Solution1()
tests = [
    (([7, 4, 3, 9, 1, 8, 5, 2, 6], 3),
     [-1, -1, -1, 5, 4, 4, -1, -1, -1]),

    (([100000], 0),
     [100000]),

    (([8], 100000),
     [-1]),
]
for inp, exp in tests:
    res = s.getAverages(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
