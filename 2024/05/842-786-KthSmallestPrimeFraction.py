"""
Leetcode
786. K-th Smallest Prime Fraction
Medium
2024-05-10

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]

 

Constraints:

    2 <= arr.length <= 1000
    1 <= arr[i] <= 3 * 10^4
    arr[0] == 1
    arr[i] is a prime number for i > 0.
    All the numbers of arr are unique and sorted in strictly increasing order.
    1 <= k <= arr.length * (arr.length - 1) / 2

 
Follow up: Can you solve the problem with better than O(n2) complexity?
"""

import heapq
from typing import List


class Solution:
    """
    Runtime: 1803 ms, faster than 21.35% of Python3 online submissions for K-th Smallest Prime Fraction.
    Memory Usage: 68.8 MB, less than 50.51% of Python3 online submissions for K-th Smallest Prime Fraction.
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        q = []
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                heapq.heappush(q, (arr[i]/arr[j], arr[i], arr[j]))

        ans = q[0]
        while q and k > 0:
            ans = heapq.heappop(q)
            k -= 1

        return [ans[1], ans[2]]


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime: 60 ms, faster than 94.24% of Python3 online submissions for K-th Smallest Prime Fraction.
    Memory Usage: 16.8 MB, less than 91.19% of Python3 online submissions for K-th Smallest Prime Fraction.
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1.0

        # Binary search for finding the kth smallest prime fraction
        while left < right:
            # Calculate the middle value
            mid = (left + right) / 2
            # Initialize variables to keep track of maximum fraction and indices
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1

            # Iterate through the array to find fractions smaller than mid
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                # Count smaller fractions
                total_smaller_fractions += (n - j)

                # If we have exhausted the array, break
                if j == n:
                    break

                # Calculate the fraction
                fraction = arr[i] / arr[j]

                # Update max_fraction and indices if necessary
                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            # Check if we have found the kth smallest prime fraction
            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                right = mid  # Adjust the range for binary search
            else:
                left = mid  # Adjust the range for binary search

        return []  # Return empty list if kth smallest prime fraction not found


class Solution2:
    """
    leetcode solution 2: Priority Queue
    Runtime: 593 ms, faster than 66.44% of Python3 online submissions for K-th Smallest Prime Fraction.
    Memory Usage: 17 MB, less than 65.76% of Python3 online submissions for K-th Smallest Prime Fraction.
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Create a priority queue to store pairs of fractions
        pq = []

        # Push the fractions formed by dividing each element by
        # the largest element into the priority queue
        for i in range(len(arr)):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))

        # Iteratively remove the top element (smallest fraction)
        # and replace it with the next smallest fraction
        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (
                    (arr[numerator_index] / arr[denominator_index]),
                    numerator_index,
                    denominator_index
                ))

        # Retrieve the kth smallest fraction from
        # the top of the priority queue
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]
