"""
Leetcode
2024-11-11
2601. Prime Subtraction Operation
Medium

You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

    Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].

Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

 

Example 1:

Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.

Example 2:

Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

Example 3:

Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
    nums.length == n
"""

import math
from typing import List


class Solution:
    """
    Runtime: 2 ms, faster than 97.77% of Python3 online submissions for Prime Subtraction Operation.
    Memory Usage: 16.8 MB, less than 35.50% of Python3 online submissions for Prime Subtraction Operation.
    """

    memo = {}

    def primeSubOperation(self, nums: List[int]) -> bool:
        nums = nums[:]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue

            reduced = self.substractPrime(nums[i], nums[i + 1])

            if reduced < 1:
                return False

            nums[i] = reduced

        return True

    def substractPrime(self, num: int, goal: int) -> int:
        low = max(num - goal + 1, 2)

        for i in range(low, num):
            if self.isPrime(i):
                return num - i

        return -1

    def isPrime(self, num) -> bool:
        if num in self.memo:
            return self.memo[num]

        is_prime = True

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break

        self.memo[num] = is_prime
        return is_prime


class Solution3:
    """
    leetcode solution 3: Sieve of Eratosthenes + Two Pointers
    Runtime: 14 ms, faster than 86.59% of Python3 online submissions for Prime Subtraction Operation.
    Memory Usage: 16.9 MB, less than 35.50% of Python3 online submissions for Prime Subtraction Operation.
    """

    def primeSubOperation(self, nums: List[int]) -> bool:
        max_element = max(nums)

        # Store the sieve array.
        sieve = [1] * (max_element + 1)
        sieve[1] = 0
        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            if sieve[i] == 1:
                for j in range(i * i, max_element + 1, i):
                    sieve[j] = 0

        # Start by storing the currValue as 1, and the initial index as 0.
        curr_value = 1
        i = 0
        while i < len(nums):
            # Store the difference needed to make nums[i] equal to currValue.
            difference = nums[i] - curr_value

            # If difference is less than 0, then nums[i] is already less than
            # currValue. Return false in this case.
            if difference < 0:
                return False

            # If the difference is prime or zero, then nums[i] can be made
            # equal to currValue.
            if sieve[difference] or difference == 0:
                i += 1
                curr_value += 1
            else:
                # Otherwise, try for the next currValue.
                curr_value += 1
        return True


s = Solution()
tests = [
    ([5, 13, 4, 13],
     False),
]
for inp, exp in tests:
    res = s.primeSubOperation(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
