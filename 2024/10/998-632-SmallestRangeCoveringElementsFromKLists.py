"""
Leetcode
2024-10-13
632. Smallest Range Covering Elements from K Lists
Hard

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

 

Constraints:

    nums.length == k
    1 <= k <= 3500
    1 <= nums[i].length <= 50
    -10^5 <= nums[i][j] <= 10^5
    nums[i] is sorted in non-decreasing order.
"""

from collections import defaultdict
import heapq
from typing import List


class Solution:
    """
    Time Limit Exceeded. 86 / 90 test cases passed.
    """

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lists_n = len(nums)
        window = [nums[i][0] for i in range(lists_n)]
        range_l, range_r = min(window), max(window)

        n = [len(nums[i]) for i in range(lists_n)]
        i = [1] * lists_n
        cur_l, cur_r = range_l, range_r
        inf = float('inf')

        changes = True
        move_right = -1

        while changes:
            changes = False
            nxt_move_right = [inf] * lists_n
            check_nxt = False

            for L in range(lists_n):
                if i[L] >= n[L]:
                    continue
                cur_num = nums[L][i[L]]
                if cur_num < cur_r or move_right == L:
                    window[L] = cur_num
                    changes = True
                    i[L] += 1
                else:
                    nxt_move_right[L] = cur_num
                    check_nxt = True

            cur_l, cur_r = min(window), max(window)
            if cur_r - cur_l < range_r - range_l:
                range_l, range_r = cur_l, cur_r
            if range_r == range_l:
                break

            if not changes and check_nxt:
                move_right = min(zip(nxt_move_right, range(lists_n)))[1]
                changes = True
            else:
                move_right = -1

        return [range_l, range_r]


class Solution1:
    """
    leetcode solution 1: Optimized brute-force
    TLE
    """

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        # Stores the current index of each list
        indices = [0] * k
        # To track the smallest range
        range_list = [0, float("inf")]

        while True:
            cur_min, cur_max = float("inf"), float("-inf")
            min_list_index = 0

            # Find the current minimum and maximum values across the lists
            for i in range(k):
                current_element = nums[i][indices[i]]

                # Update the current minimum
                if current_element < cur_min:
                    cur_min = current_element
                    min_list_index = i

                # Update the current maximum
                if current_element > cur_max:
                    cur_max = current_element

            # Update the range if a smaller one is found
            if cur_max - cur_min < range_list[1] - range_list[0]:
                range_list[0] = cur_min
                range_list[1] = cur_max

            # Move to the next element in the list that had the minimum value
            indices[min_list_index] += 1
            if indices[min_list_index] == len(nums[min_list_index]):
                break

        return range_list


class Solution2:
    """
    leetcode solution 2: Priority Queue (Heap)
    Runtime: 205 ms, faster than 29.05% of Python3 online submissions for Smallest Range Covering Elements from K Lists.
    Memory Usage: 23.1 MB, less than 79.95% of Python3 online submissions for Smallest Range Covering Elements from K Lists.
    """

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Priority queue to store (value, list index, element index)
        pq = []
        max_val = float("-inf")
        range_start = 0
        range_end = float("inf")

        # Insert the first element from each list into the min-heap
        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        # Continue until we can't proceed further
        while len(pq) == len(nums):
            min_val, row, col = heapq.heappop(pq)

            # Update the smallest range
            if max_val - min_val < range_end - range_start:
                range_start = min_val
                range_end = max_val

            # If possible, add the next element from the same row to the heap
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(pq, (next_val, row, col + 1))
                max_val = max(max_val, next_val)

        return [range_start, range_end]


class Solution3:
    """
    leetcode solution 3: Two Pointer
    Runtime: 192 ms, faster than 62.63% of Python3 online submissions for Smallest Range Covering Elements from K Lists.
    Memory Usage: 24.5 MB, less than 13.01% of Python3 online submissions for Smallest Range Covering Elements from K Lists.
    """

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []

        # Merge all lists with their list index
        for i in range(len(nums)):
            for num in nums[i]:
                merged.append((num, i))

        # Sort the merged list
        merged.sort()

        # Two pointers to track the smallest range
        freq = defaultdict(int)
        left, count = 0, 0
        range_start, range_end = 0, float("inf")

        for right in range(len(merged)):
            freq[merged[right][1]] += 1
            if freq[merged[right][1]] == 1:
                count += 1

            # When all lists are represented, try to shrink the window
            while count == len(nums):
                cur_range = merged[right][0] - merged[left][0]
                if cur_range < range_end - range_start:
                    range_start = merged[left][0]
                    range_end = merged[right][0]

                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    count -= 1
                left += 1

        return [range_start, range_end]


s = Solution()
tests = [
    ([[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5]],
     [-1, 1]),

    ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],
     [20, 24]),

    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]],
     [1, 1]),

    ([[10, 10], [11, 11]],
     [10, 11]),
]
for inp, exp in tests:
    res = s.smallestRange(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
