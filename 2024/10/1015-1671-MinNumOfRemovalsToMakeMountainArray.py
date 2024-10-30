"""
Leetcode
2024-10-30
1671. Minimum Number of Removals to Make Mountain Array
Hard

You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array nums, return the minimum number of elements to remove to make nums a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

 

Constraints:

    3 <= nums.length <= 1000
    1 <= nums[i] <= 10^9
    It is guaranteed that you can make a mountain array out of nums.
"""

from typing import List


class Solution:
    """
    Wrong Answer
    """

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp_right = [1] * n
        dp_left = [1] * n

        # left to right
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp_right[i] = max(dp_right[i], dp_right[j] + 1)

        # right to left
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]:
                    dp_left[i] = max(dp_left[i], dp_left[j] + 1)

        return n - max(dp_right[i] + dp_left[i] for i in range(1, n-1)) + 1


class Solution1:
    """
    leetcode solution 1: LIS Using Dynamic Programming
    Runtime: 1843 ms, faster than 55.81% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
    Memory Usage: 16.9 MB, less than 13.17% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
    """

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = [1] * N
        lds_length = [1] * N

        # Stores the length of longest increasing subsequence that ends at i.
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)

        # Stores the length of longest decreasing subsequence that starts at i.
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals


class Solution2:
    """
    leetcode solution 2: LIS Using Binary Search
    Runtime: 39 ms, faster than 76.74% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
    Memory Usage: 16.9 MB, less than 31.03% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
    """

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = self.getLongestIncreasingSubsequenceLength(nums)

        nums.reverse()
        lds_length = self.getLongestIncreasingSubsequenceLength(nums)
        # Reverse the length array to correctly depict the lenght of longest decreasing subsequnec for each index.
        lds_length.reverse()

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals

    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]

        for i in range(1, len(v)):
            index = self.lowerBound(lis, v[i])

            # Add to the list if v[i] is greater than the last element
            if index == len(lis):
                lis.append(v[i])
            else:
                # Replace the element at index with v[i]
                lis[index] = v[i]

            lis_len[i] = len(lis)

        return lis_len

    # Returns the index of the first element which is equal to or greater than target.
    def lowerBound(self, lis: List[int], target: int) -> int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
