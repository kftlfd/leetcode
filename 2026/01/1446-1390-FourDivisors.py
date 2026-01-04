"""
Leetcode
2026-01-04
1390. Four Divisors
Medium

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Example 2:

Input: nums = [21,21]
Output: 64

Example 3:

Input: nums = [1,2,3,4,5]
Output: 0

 

Constraints:

    1 <= nums.length <= 10^4
    1 <= nums[i] <= 10^5


Hint 1
Find the divisors of each element in the array.
Hint 2
You only need to loop to the square root of a number to find its divisors.
"""

import math
from typing import List


class Solution:
    """
    Runtime 235ms Beats 41.12%
    Memory 18.62MB Beats 87.80%    
    """

    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divisors(num: int):
            divisors_count = 2
            divisors_sum = 1 + num
            for i in range(2, math.floor(math.sqrt(num)) + 1):
                div, rem = divmod(num, i)
                if rem != 0:
                    continue
                divisors_count += 1
                divisors_sum += i
                if div != i:
                    divisors_count += 1
                    divisors_sum += div
                if divisors_count > 4:
                    return False, 0
            if divisors_count != 4:
                return False, 0
            return True, divisors_sum

        ans = 0
        for num in nums:
            if num < 6:
                continue
            is4divs, count = get_divisors(num)
            if is4divs:
                ans += count

        return ans


class Solution1:
    """
    sample 193 ms solution
    Runtime 201ms Beats 47.04%
    Memory 18.69MB Beats 87.80%
    """

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = set()
            for i in range(1, int(math.sqrt(n)+1)):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        return total


class Solution2:
    """
    sample 103 ms solution
    Runtime 106ms Beats 87.11%
    Memory 18.63MB Beats 87.80%
    """

    def sumFourDivisors(self, nums: List[int]) -> int:
        def isPrime(x):
            if x < 2:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        ans = 0

        for n in nums:
            p = round(n ** (1/3))
            if p*p*p == n and isPrime(p):
                ans += 1 + p + p*p + n
                continue

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    p = i
                    q = n // i
                    if p != q and isPrime(p) and isPrime(q):
                        ans += 1 + p + q + n
                    break

        return ans
