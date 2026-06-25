"""
Leetcode
2026-06-25
3737. Count Subarrays With Majority Element I
Medium

You are given an integer array nums and an integer target.

Return the number of of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

 

Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

    nums[1..1] = [2]
    nums[2..2] = [2]
    nums[1..2] = [2,2]
    nums[0..2] = [1,2,2]
    nums[1..3] = [2,2,3]

So there are 5 such subarrays.

Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

All 10 subarrays have 1 as the majority element.

Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^9
    1 <= target <= 10^9

    
Hint 1
Use brute force
Hint 2
Count all subarrays where 2 * count(target) > length
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        return sum(self._is_maj_el(arr, target) for arr in self._get_arrs(nums))

    def _get_arrs(self, arr: list[int]):
        n = len(arr)
        for l in range(n + 1):
            for s in range(n - l):
                yield arr[s:s+l+1]

    def _is_maj_el(self, arr: list[int], target: int) -> bool:
        return 2 * arr.count(target) > len(arr)


class Solution01:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        def check(arr: list[int]):
            return 2 * arr.count(target) > len(arr)

        return sum(map(check, self._get_arrs(nums)))

    def _get_arrs(self, arr: list[int]):
        n = len(arr)
        for l in range(n + 1):
            for s in range(n - l):
                yield arr[s:s+l+1]


class Solution1:
    """
    leetcode solution: Enumeration
    Runtime 1370ms Beats 64.89%
    Memory 19.45MB Beats 64.89%
    """

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += 1 if nums[j] == target else -1
                if cnt > 0:
                    ans += 1
        return ans


class Solution2:
    """
    sample 34ms solution
    Runtime 11ms Beats 99.11%
    Memory 19.59MB Beats 30.22%
    """

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        t = target
        cnt = [0] * (n*2+2)
        acc = [0] * (n*2+2)
        pre = n+1
        cnt[pre] = 1
        acc[pre] = 1
        res = 0
        for num in nums:
            if t == num:
                pre += 1
            else:
                pre -= 1
            cnt[pre] += 1
            acc[pre] = acc[pre-1] + cnt[pre]
            res += acc[pre-1]
        return res
