"""
Leetcode
2025-03-29
2818. Apply Operations to Maximize Score
Hard

You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

    Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
    Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
    Multiply your score by x.

Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [8,3,9,3,8], k = 2
Output: 81
Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.

Example 2:

Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788
Explanation: To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.

 

Constraints:

    1 <= nums.length == n <= 10^5
    1 <= nums[i] <= 10^5
    1 <= k <= min(n * (n + 1) / 2, 10^9)


Hint 1
Calculate nums[i]'s prime score s[i] by factoring in O(sqrt(nums[i])) time.
Hint 2
For each nums[i], find the nearest index left[i] on the left (if any) such that s[left[i]] >= s[i]. if none is found, set left[i] to -1. Similarly, find the nearest index right[i] on the right (if any) such that s[right[i]] > s[i]. If none is found, set right[i] to n.
Hint 3
Use a monotonic stack to compute right[i] and left[i].
Hint 4
For each index i, if left[i] + 1 <= l <= i <= r <= right[i] - 1, then s[i] is the maximum value in the range [l, r]. For this particular i, there are ranges[i] = (i - left[i]) * (right[i] - i) ranges where index i will be chosen.
Hint 5
Loop over all elements of nums by non-increasing prime score, each element will be chosen min(ranges[i], remainingK) times, where reaminingK denotes the number of remaining operations. Therefore, the score will be multiplied by s[i]^min(ranges[i],remainingK).
Hint 6
Use fast exponentiation to quickly calculate A^B mod C.
"""

from collections import deque
import heapq
import math
from typing import List


class Solution1:
    """
    leetcode solution 1: Monotonic Stack & Priority Queue
    Runtime 3612ms Beats 37.07%
    Memory 44.96MB Beats 62.07%
    """

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        n = len(nums)
        prime_scores = [0] * n

        # Calculate the prime score for each number in nums
        for index in range(n):
            num = nums[index]

            # Check for prime factors from 2 to sqrt(n)
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    # Increment prime score for each prime factor
                    prime_scores[index] += 1

                    # Remove all occurrences of the prime factor from num
                    while num % factor == 0:
                        num //= factor

            # If num is still greater than or equal to 2, it's a prime factor
            if num >= 2:
                prime_scores[index] += 1

        # Initialize next and previous dominant index arrays
        next_dominant = [n] * n
        prev_dominant = [-1] * n

        # Stack to store indices for monotonic decreasing prime score
        decreasing_prime_score_stack = []

        # Calculate the next and previous dominant indices for each number
        for index in range(n):
            # While the stack is not empty and the current prime score is greater than the stack's top
            while (
                decreasing_prime_score_stack
                and prime_scores[decreasing_prime_score_stack[-1]]
                < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()

                # Set the next dominant element for the popped index
                next_dominant[top_index] = index

            # If the stack is not empty, set the previous dominant element for the current index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]

            # Push the current index onto the stack
            decreasing_prime_score_stack.append(index)

        # Calculate the number of subarrays in which each element is dominant
        num_of_subarrays = [0] * n
        for index in range(n):
            num_of_subarrays[index] = (next_dominant[index] - index) * (
                index - prev_dominant[index]
            )

        # Priority queue to process elements in decreasing order of their value
        processing_queue = []

        # Push each number and its index onto the priority queue
        for index in range(n):
            heapq.heappush(processing_queue, (-nums[index], index))

        score = 1

        # Helper function to compute the power of a number modulo MOD
        def _power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:
                # If the exponent is odd, multiply the result by the base
                if exponent % 2 == 1:
                    res = (res * base) % MOD

                # Square the base and halve the exponent
                base = (base * base) % MOD
                exponent //= 2

            return res

        # Process elements while there are operations left
        while k > 0:
            # Get the element with the maximum value from the queue
            num, index = heapq.heappop(processing_queue)
            num = -num  # Negate back to positive

            # Calculate the number of operations to apply on the current element
            operations = min(k, num_of_subarrays[index])

            # Update the score by raising the element to the power of operations
            score = (score * _power(num, operations)) % MOD

            # Reduce the remaining operations count
            k -= operations

        return score


class Solution2:
    """
    leetcode solution 2: Sieve of Eratosthenes & Sorting
    Runtime 2903ms Beats 70.69%
    Memory 44.95MB Beats 62.07%
    """

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = int(1e9 + 7)

        n = len(nums)
        prime_scores = [0] * n

        # Find the maximum element in nums to determine the range for prime generation
        max_element = max(nums)

        # Get all prime numbers up to max_element using the Sieve of Eratosthenes
        primes = self.get_primes(max_element)

        # Calculate the prime score for each number in nums
        for index in range(n):
            num = nums[index]

            # Iterate over the generated primes to count unique prime factors
            for prime in primes:
                if prime * prime > num:
                    break  # Stop early if prime^2 exceeds num
                if num % prime != 0:
                    continue  # Skip if the prime is not a factor

                # Increment prime score for the factor
                prime_scores[index] += 1
                while num % prime == 0:
                    num //= prime  # Remove all occurrences of this factor

            # If num is still greater than 1, it is a prime number itself
            if num > 1:
                prime_scores[index] += 1

        # Initialize next and previous dominant index arrays
        next_dominant = [n] * n
        prev_dominant = [-1] * n

        # Stack to store indices for a monotonic decreasing prime score
        decreasing_prime_score_stack = deque()

        # Calculate the next and previous dominant indices for each number
        for index in range(n):
            # While the stack is not empty and the current prime score is
            # greater than the stack's top, update next_dominant
            while (
                decreasing_prime_score_stack
                and prime_scores[decreasing_prime_score_stack[-1]]
                < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()

                # Set the next dominant element for the popped index
                next_dominant[top_index] = index

            # If the stack is not empty, set the previous dominant element for
            # the current index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]

            # Push the current index onto the stack
            decreasing_prime_score_stack.append(index)

        # Calculate the number of subarrays in which each element is dominant
        num_of_subarrays = [
            (next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)
        ]

        # Sort elements in decreasing order based on their values
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1

        # Helper function to compute the power of a number modulo MOD
        def _power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:
                # If the exponent is odd, multiply the result by the base
                if exponent % 2:
                    res = (res * base) % MOD

                # Square the base and halve the exponent
                base = (base * base) % MOD
                exponent //= 2

            return res

        processing_index = 0

        # Process elements while there are operations left
        while k > 0:
            # Get the element with the maximum value
            index, num = sorted_array[processing_index]
            processing_index += 1

            # Calculate the number of operations to apply on the current
            # element
            operations = min(k, num_of_subarrays[index])

            # Update the score by raising the element to the power of
            # operations
            score = (score * _power(num, operations)) % MOD

            # Reduce the remaining operations count
            k -= operations

        return score

    # Function to generate prime numbers up to a given limit using the Sieve of Eratosthenes
    def get_primes(self, limit: int) -> List[int]:
        is_prime = [True] * (limit + 1)
        primes = []

        # Start marking from the first prime number (2)
        for number in range(2, limit + 1):
            if not is_prime[number]:
                continue

            # Store the prime number
            primes.append(number)

            # Mark multiples of the prime number as non-prime
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

        return primes
