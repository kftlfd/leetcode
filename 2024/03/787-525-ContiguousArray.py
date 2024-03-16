"""
Leetcode
525. Contiguous Array
Medium
2024-03-16

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = 0
        prefix_sums = [0] * (n + 1)
        ans = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sums[i + 1] = prefix_sum

        for start in range(n):
            for end in range(start + 1, n, 2):
                if prefix_sums[end + 1] - prefix_sums[start] == (end - start + 1) // 2:
                    ans = max(ans, end - start + 1)

        return ans


class Solution2:
    """
    leetcode solution 2 Using Extra Array
    Runtime: 611 ms, faster than 77.56% of Python3 online submissions for Contiguous Array.
    Memory Usage: 19.3 MB, less than 99.44% of Python3 online submissions for Contiguous Array.
    """

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [-2] * (2 * n + 1)
        arr[n] = -1
        maxlen = 0
        count = 0

        for i in range(n):
            count += -1 if nums[i] == 0 else 1

            if arr[count + n] >= -1:
                maxlen = max(maxlen, i - arr[count + n])
            else:
                arr[count + n] = i

        return maxlen


class Solution3:
    """
    leetcode solution 3 Using HashMap
    Runtime: 600 ms, faster than 92.23% of Python3 online submissions for Contiguous Array.
    Memory Usage: 22.3 MB, less than 32.12% of Python3 online submissions for Contiguous Array.
    """

    def findMaxLength(self, nums: List[int]) -> int:
        hm = {0: -1}
        n = len(nums)
        maxlen = 0
        count = 0

        for i in range(n):
            count += 1 if nums[i] == 1 else -1

            if count in hm:
                maxlen = max(maxlen, i - hm[count])
            else:
                hm[count] = i

        return maxlen


s = Solution()
tests = [
    ([0, 0, 1, 0, 0, 0, 1, 1],
     6),

    ([0, 1],
     2),

    ([0, 1, 0],
     2),
]
for inp, exp in tests:
    res = s.findMaxLength(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
