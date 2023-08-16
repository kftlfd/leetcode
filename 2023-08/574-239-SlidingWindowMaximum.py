"""
Leetcode
239. Sliding Window Maximum (hard)
2023-08-16

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""

from typing import List
from collections import deque


class Solution:
    """
    leetcode solution: monotonic stack
    Runtime: 1283 ms, faster than 97.02% of Python3 online submissions for Sliding Window Maximum.
    Memory Usage: 33.2 MB, less than 64.81% of Python3 online submissions for Sliding Window Maximum.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        ans.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])

        return ans


s = Solution()
tests = [
    (([1, 3, -1, -3, 5, 3, 6, 7], 3),
     [3, 3, 5, 5, 6, 7]),

    (([1], 1),
     [1]),
]
for inp, exp in tests:
    res = s.maxSlidingWindow(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
