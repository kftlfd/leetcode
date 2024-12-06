"""
Leetcode
2024-12-06
2554. Maximum Number of Integers to Choose From a Range I
Medium

You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

    The chosen integers have to be in the range [1, n].
    Each integer can be chosen at most once.
    The chosen integers should not be in the array banned.
    The sum of the chosen integers should not exceed maxSum.

Return the maximum number of integers you can choose following the mentioned rules.

 

Example 1:

Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.

Example 2:

Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.

Example 3:

Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.

 

Constraints:

    1 <= banned.length <= 10^4
    1 <= banned[i], n <= 10^4
    1 <= maxSum <= 10^9
"""

from typing import List


class Solution01:
    """
    Time Limit Exceeded
    """

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        nums = []
        for i in range(1, n+1):
            if i not in banned_set:
                nums.append(i)
        ln = len(nums)

        ans = [0]

        def dfs(i: int, count: int, cur_sum: 0):
            if cur_sum > maxSum:
                return

            ans[0] = max(ans[0], count)

            if i >= ln:
                return

            # pick
            dfs(i+1, count+1, cur_sum + nums[i])

            # skip
            dfs(i+1, count, cur_sum)

        dfs(0, 0, 0)

        return ans[0]


class Solution02:
    """
    Runtime: 38 ms, faster than 88.16% of Python3 online submissions for Maximum Number of Integers to Choose From a Range I.
    Memory Usage: 19 MB, less than 9.90% of Python3 online submissions for Maximum Number of Integers to Choose From a Range I.
    """

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        cur_sum = 0
        ans = 0

        for num in range(1, n+1):
            if num in banned_set:
                continue
            cur_sum += num
            if cur_sum > maxSum:
                break
            ans += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime: 471 ms, faster than 6.14% of Python3 online submissions for Maximum Number of Integers to Choose From a Range I.
    Memory Usage: 18.5 MB, less than 43.45% of Python3 online submissions for Maximum Number of Integers to Choose From a Range I.
    """

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Sort banned array to enable binary search
        banned.sort()
        count = 0

        # Try each number from 1 to n
        for num in range(1, n + 1):
            # Skip if number is in banned array
            if self._custom_binary_search(banned, num):
                continue

            maxSum -= num
            # Break if sum exceeds our limit
            if maxSum < 0:
                break

            count += 1

        return count

    def _custom_binary_search(self, arr: List[int], target: int) -> bool:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
