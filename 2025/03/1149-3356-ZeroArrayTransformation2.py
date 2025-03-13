"""
Leetcode
2025-03-13
3356. Zero Array Transformation II
Medium

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

    For i = 0 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [1, 0, 1].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

    For i = 0 (l = 1, r = 3, val = 2):
        Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
        The array will become [4, 1, 0, 0].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
        The array will become [3, 0, 0, 0], which is not a Zero Array.

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 5 * 10^5
    1 <= queries.length <= 10^5
    queries[i].length == 3
    0 <= li <= ri < nums.length
    1 <= vali <= 5


Hint 1
Can we apply binary search here?
Hint 2
Utilize a difference array to optimize the processing of queries.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def can_make_zero_arr(k: int) -> bool:
            arr = [0] * len(nums)
            for left, right, val in queries[:k]:
                for i in range(left, right+1):
                    arr[i] += val
            return all(a >= b for a, b in zip(arr, nums))

        left = 0
        right = len(queries) + 1
        while left < right:
            mid = (left + right) // 2
            if can_make_zero_arr(mid):
                right = mid
            else:
                left = mid + 1

        return left if left <= len(queries) else -1


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime 696ms Beats 60.68%
    Memory 63.23MB Beats 56.40%
    """

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # n = len(nums)
        left, right = 0, len(queries)

        # Zero array isn't formed after all queries are processed
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    def can_form_zero_array(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if zero array can be formed
        for num_index in range(n):
            total_sum += difference_array[num_index]
            if total_sum < nums[num_index]:
                return False
        return True


class Solution2:
    """
    leetcode solution 2: Line Sweep
    Runtime 146ms Beats 89.66%
    Memory 62.86MB Beats 99.10%
    """

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        # Iterate through nums
        for index in range(n):
            # Iterate through queries while current index of nums cannot equal zero
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                # Zero array isn't formed after all queries are processed
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Process start and end of range
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            # Update prefix sum at current index
            total_sum += difference_array[index]

        return k
