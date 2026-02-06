"""
Leetcode
2026-02-06
3634. Minimum Removals to Balance Array
Medium
Topics
premium lock iconCompanies
Hint

You are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

 

Example 1:

Input: nums = [2,1,5], k = 2

Output: 1

Explanation:

    Remove nums[2] = 5 to get nums = [2, 1].
    Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.

Example 2:

Input: nums = [1,6,2,9], k = 3

Output: 2

Explanation:

    Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
    Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.

Example 3:

Input: nums = [4,6], k = 2

Output: 0

Explanation:

    Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= 10^5

 
Hint 1
Sort nums and use two pointers i and j so that the window's minimum is nums[i] and maximum is nums[j].
Hint 2
Expand j while nums[j] <= k * nums[i] to maximize the balanced window; answer = n - (j - i + 1).
"""

from typing import List


class Solution01:
    """
    Time Limit Exceeded
    """

    def minRemoval(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        for removals in range(n):
            for i in range(removals + 1):
                if nums[i] * k >= nums[(n - 1 - removals) + i]:
                    return removals

        return -1


class Solution02:
    """
    Runtime 329ms Beats 7.22%
    Memory 33.82MB Beats 42.24%
    """

    def minRemoval(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        def check(removals: int) -> bool:
            for i in range(removals + 1):
                if nums[i] * k >= nums[(n - 1 - removals) + i]:
                    return True
            return False

        l = 0
        r = n - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


class Solution1:
    """
    leetcode solution: Sorting + Two Pointers
    Runtime 154ms Beats 49.10%
    Memory 34.73MB Beats 16.25%
    """

    def minRemoval(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            ans = min(ans, n - (right - left))

        return ans
