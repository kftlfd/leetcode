"""
Leetcode
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
Medium
2024-07-03

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.

Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.

 

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List

from heapq import heappush, heappushpop, heappop, nlargest, nsmallest


class Solution:
    """
    Runtime: 249 ms, faster than 95.76% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
    Memory Usage: 27.4 MB, less than 39.86% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
    """

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        smallest = []
        largest = []

        for num in nums[:4]:
            heappush(smallest, -num)
            heappush(largest, num)

        for num in nums[4:]:
            heappushpop(smallest, -num)
            heappushpop(largest, num)

        mins = [-heappop(smallest) for _ in range(4)][::-1]
        maxs = [heappop(largest) for _ in range(4)]

        min_diff = float('inf')
        for i in range(4):
            min_diff = min(min_diff, abs(maxs[i] - mins[i]))

        return min_diff


class Solution2:
    """
    leetcode solution 2: Partial Sort + Greedy Deletion
    Runtime: 244 ms, faster than 97.88% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
    Memory Usage: 27.9 MB, less than 12.26% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
    """

    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0

        # Find the four smallest elements
        smallest_four = sorted(nsmallest(4, nums))

        # Find the four largest elements
        largest_four = sorted(nlargest(4, nums))

        min_diff = float("inf")
        # Four scenarios to compute the minimum difference
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])

        return min_diff
