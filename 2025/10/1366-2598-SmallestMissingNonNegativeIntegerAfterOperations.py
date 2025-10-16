"""
Leetcode
2025-10-16
2598. Smallest Missing Non-negative Integer After Operations
Medium

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

    For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].

The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

    For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.

Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.

Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.

 

Constraints:

    1 <= nums.length, value <= 10^5
    -10^9 <= nums[i] <= 10^9


Hint 1
Think about using modular arithmetic.
Hint 2
if x = nums[i] (mod value), then we can make nums[i] equal to x after some number of operations
Hint 3
How does finding the frequency of (nums[i] mod value) help?
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    """
    Runtime 159ms Beats 55.23%
    Memory 38.42MB Beats 58.49%
    """

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num % value] += 1

        ans = 0
        while True:
            i = ans % value
            if cnt[i] < 1:
                break
            cnt[i] -= 1
            ans += 1

        return ans


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 193ms Beats 23.96%
    Memory 38.55MB Beats 48.26%
    """

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = Counter(x % value for x in nums)
        mex = 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        return mex


class Solution2:
    """
    sample 46ms solution
    Runtime 42ms Beats 94.26%
    Memory 31.39MB Beats 98.65%
    """

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        mods = [0] * value
        for num in nums:
            mods[num % value] += 1
        min_i, min_mod = n + 1, n + 1
        for i, mod in enumerate(mods):
            if mod < min_mod:
                min_i = i
                min_mod = mod
        return min_mod * value + min_i
