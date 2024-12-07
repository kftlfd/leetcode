"""
Leetcode
2024-12-07
1760. Minimum Limit of Balls in a Bag
Medium

You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

    Take any bag of balls and divide it into two new bags with a positive number of balls.
        For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.

Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

 

Example 1:

Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

Example 2:

Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= maxOperations, nums[i] <= 10^9

Hints:
- Let's change the question if we know the maximum size of a bag what is the minimum number of bags you can make
- note that as the maximum size increases the minimum number of bags decreases so we can binary search the maximum size
"""

from math import ceil
from typing import List


class Solution:
    """
    Runtime: 767 ms, faster than 41.58% of Python3 online submissions for Minimum Limit of Balls in a Bag.
    Memory Usage: 29.5 MB, less than 19.09% of Python3 online submissions for Minimum Limit of Balls in a Bag.
    """

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def ops_required(size: int) -> int:
            ops = 0
            for num in nums:
                if num <= size:
                    continue
                ops += ceil(num / size) - 1
            return ops

        lo = 1
        hi = max(nums)
        ans = hi
        while lo < hi:
            mid = (lo + hi) // 2
            if ops_required(mid) <= maxOperations:
                ans = mid
                hi = mid
            else:
                lo = mid + 1

        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 868 ms, faster than 24.21% of Python3 online submissions for Minimum Limit of Balls in a Bag.
    Memory Usage: 29.2 MB, less than 30.91% of Python3 online submissions for Minimum Limit of Balls in a Bag.
    """

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Binary search bounds
        left = 1
        right = max(nums)

        # Perform binary search to find the optimal max_balls_in_bag
        while left < right:
            middle = (left + right) // 2

            # Check if a valid distribution is possible with the current middle value
            if self._is_possible(middle, nums, maxOperations):
                # If possible, try a smaller value (shift right to middle)
                right = middle
            else:
                # If not possible, try a larger value (shift left to middle + 1)
                left = middle + 1

        # Return the smallest possible value for max_balls_in_bag
        return left

    # Helper function to check if a distribution is possible for a given max_balls_in_bag
    def _is_possible(self, max_balls_in_bag, nums, max_operations):
        total_operations = 0

        # Iterate through each bag in the array
        for num in nums:
            # Calculate the number of operations needed to split this bag
            operations = ceil(num / max_balls_in_bag) - 1
            total_operations += operations

            # If total operations exceed max_operations, return False
            if total_operations > max_operations:
                return False

        # We can split the balls within the allowed operations, return True
        return True
