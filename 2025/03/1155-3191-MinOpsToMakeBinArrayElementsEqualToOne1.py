"""
Leetcode
2025-03-19
3191. Minimum Operations to Make Binary Array Elements Equal to One I
Medium
Topics
Companies
Hint

You are given a

nums.

You can do the following operation on the array any number of times (possibly zero):

    Choose any 3 consecutive elements from the array and flip all of them.

Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

Example 1:

Input: nums = [0,1,1,1,0,0]

Output: 3

Explanation:
We can do the following operations:

    Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
    Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
    Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

Example 2:

Input: nums = [0,1,1,1]

Output: -1

Explanation:
It is impossible to make all elements equal to 1.

 

Constraints:

    3 <= nums.length <= 10^5
    0 <= nums[i] <= 1


Hint 1
If nums[0] is 0, then the only way to change it to 1 is by doing an operation on the first 3 elements of the array.
Hint 2
After Changing nums[0] to 1, use the same logic on the remaining array.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 63ms Beats 100.00%
    Memory 21.62MB Beats 54.50%
    """

    def minOperations(self, nums: List[int]) -> int:
        a = 1
        b = nums[0]
        c = nums[1]
        ops = 0

        for right in range(2, len(nums)):
            if a == 0:
                ops += 1
                a = b ^ 1
                b = c ^ 1
                c = nums[right]
            else:
                a = b
                b = c
                c = nums[right]

        if a == 0:
            ops += 1
            a ^= 1
            b ^= 1
            c ^= 1

        return ops if (b == 1 and c == 1) else -1


class Solution1:
    """
    leetcode solution 1: Using Deque
    Runtime 169ms Beats 27.25%
    Memory 21.82MB Beats 9.51%
    """

    def minOperations(self, nums: List[int]) -> int:
        flip_queue = deque()  # Stores indices of flip operations
        count = 0  # Number of operations performed

        for i, num in enumerate(nums):
            # Remove expired flips (older than 3 indices)
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()

            # If the current element needs flipping
            if (num + len(flip_queue)) % 2 == 0:
                # Cannot flip a full triplet
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flip_queue.append(i)

        return count


class Solution2:
    """
    leetcode solution 2: Sliding Window
    Runtime 115ms Beats 55.27%
    Memory 21.66MB Beats 54.50%
    """

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(2, len(nums)):

            # only looking forward to the last element
            if nums[i - 2] == 0:
                count += 1
                # flip i-2 and i-1 and i
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == len(nums):
            return count
        return -1


class Solution3:
    """
    leetcode solution 3: Bit Manipulation & Greedy
    Runtime 82ms Beats 94.86%
    Memory 21.44MB Beats 96.40%
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1

        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1
        return count
