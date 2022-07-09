"""
Leetcode
1696. Jump Game VI (medium)
2022-07-09

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
"""

from typing import List


# Time Limit Exceeded (57 / 71 test cases passed.)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[-k:]) + nums[i])
        return dp[-1]


# https://leetcode.com/problems/jump-game-vi/discuss/978497/Python-DP-+-Sliding-Window-Maximum-problem-combined
# Runtime: 1009 ms, faster than 97.33% of Python3 online submissions for Jump Game VI.
# Memory Usage: 27.5 MB, less than 75.31% of Python3 online submissions for Jump Game VI.
class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]

            while d and d[-1][0] < dp[i]:
                d.pop()
            d.append((dp[i], i))

            if i-k == d[0][1]:
                d.popleft()

        return dp[-1]


s = Solution2()
tests = [
    ([1, -1, -2, 4, -7, 3], 2),
    ([10, -5, -2, 4, 0, 3], 3),
    ([1, -5, -20, 4, -1, 3, -6, -3], 2),
]
for t in tests:
    print(t)
    print(s.maxResult(t[0], t[1]))
    print()
