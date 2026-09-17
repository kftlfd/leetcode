"""
Leetcode
2026-09-17
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Medium

You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

 

Constraints:

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 1000
    1 <= target <= 10^8


"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        pref = [INF] * n
        min_len = n
        for i in range(n):
            cur_sum = 0
            j = i - 1
            while j >= 0 and cur_sum < target:
                cur_sum += arr[j]
                j -= 1
            if cur_sum == target:
                min_len = min(min_len, i - 1 - j)
            if min_len == 1:
                for i in range(i, n):
                    pref[i] = 1
                break
            pref[i] = min_len

        if min_len == n:
            return -1

        suff = [INF] * n
        min_len = n
        for i in range(n - 1, -1, -1):
            cur_sum = arr[i]
            j = i + 1
            while j < n and cur_sum < target:
                cur_sum += arr[j]
                j += 1
            if cur_sum == target:
                min_len = min(min_len, j - i)
            if min_len == 1:
                for i in range(i + 1):
                    suff[i] = 1
                break
            suff[i] = min_len

        ans = INF
        for l, r in zip(pref, suff):
            if l > 0 and r > 0 and l + r < ans:
                ans = l + r

        return ans if ans < INF else -1


class Solution1:
    """
    leetcode solution 1: Prefix Sum + Dynamic Programming + Hash Table
    Runtime 147ms Beats 57.54%
    Memory 39.21MB Beats 46.93%
    """

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pos = {0: -1}
        n = len(arr)
        s = 0
        ans = n + 1
        min_l = n
        for i, x in enumerate(arr):
            s += x
            if s - target in pos:
                j = pos[s - target]
                length = i - j
                ans = min(ans, length + (n if j == -1 else arr[j]))
                min_l = min(min_l, length)
            arr[i] = min_l
            pos[s] = i
        return -1 if ans == n + 1 else ans


class Solution2:
    """
    leetcode solution 2: Sliding Window + Dynamic Programming
    Runtime 115ms Beats 69.27%
    Memory 31.07MB Beats 83.24%
    """

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n, ans, total = len(arr), len(arr) + 1, 0
        dp = [n] * (n + 1)
        left = 0
        for right, x in enumerate(arr):
            total += x
            while total > target:
                total -= arr[left]
                left += 1
            dp[right + 1] = dp[right]
            if total == target:
                ans = min(ans, right - left + 1 + dp[left])
                dp[right + 1] = min(dp[right], right - left + 1)
        return -1 if ans == n + 1 else ans
