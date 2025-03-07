"""
Leetcode
2025-03-07
2523. Closest Prime Numbers in Range
Medium

Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right .
    Both num1 and num2 are 

    .
    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

 

Constraints:

    1 <= left <= right <= 10^6


Hint 1
Use Sieve of Eratosthenes to mark numbers that are primes.
Hint 2
Iterate from right to left and find pair with the minimum distance between marked numbers.
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Sieve of Eratosthenes
    Runtime 1459ms Beats 59.06%
    Memory 35.08MB Beats 26.56%
    """

    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Get all prime numbers up to 'right' using sieve
        sieve_array = self._sieve(right)

        prime_numbers = [
            num for num in range(left, right + 1) if sieve_array[num]
        ]

        # Step 2: Find the closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1  # Less than two primes

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]

        return closest_pair

    def _sieve(self, upper_limit):
        # Create an integer list to mark prime numbers (True = prime, False = not prime)
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                # Mark all multiples of 'number' as non-prime
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve


class Solution2:
    """
    leetcode solution 2: Analyze Distance between twin primes
    Runtime 4ms Beats 91.88%
    Memory 17.86MB Beats 89.06%
    """

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev_prime = -1
        closestA = -1
        closestB = -1
        min_difference = float("inf")

        # Iterate over the range of numbers and find primes
        for candidate in range(left, right + 1):
            if self.isPrime(candidate):
                if prev_prime != -1:
                    difference = candidate - prev_prime
                    if difference < min_difference:
                        min_difference = difference
                        closestA = prev_prime
                        closestB = candidate
                    if difference == 1 or difference == 2:
                        return [prev_prime, candidate]
                prev_prime = candidate

        return [closestA, closestB] if closestA != -1 else [-1, -1]

    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True
