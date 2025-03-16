"""
Leetcode
2025-03-16
2594. Minimum Time to Repair Cars
Medium

You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.

Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.


Constraints:

    1 <= ranks.length <= 10^5
    1 <= ranks[i] <= 100
    1 <= cars <= 10^6


Hint 1
For a predefined fixed time, can all the cars be repaired?
Hint 2
Try using binary search on the answer.
"""

from collections import Counter
from heapq import heapify, heappop, heappush
import math
from typing import List


class Solution1:
    """
    leetcode solution 1: Binary Search on Time
    Runtime 80ms Beats 93.22%
    Memory 21.99MB Beats 49.42%
    """

    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_rank, max_rank = ranks[0], ranks[0]

        # Find min and max rank dynamically
        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)

        # Frequency list to count mechanics with each rank
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            min_rank = min(min_rank, rank)
            freq[rank] += 1

        # Minimum possible time, Maximum possible time
        low = 1
        high = min_rank * cars * cars

        # Perform binary search to find the minimum time required
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0

            # Calculate the total number of cars that can be repaired in 'mid' time
            for rank in range(1, max_rank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))

            # Adjust the search boundaries based on the number of cars repaired
            if cars_repaired >= cars:
                high = mid  # Try to find a smaller time
            else:
                low = mid + 1  # Need more time

        return low


class Solution2:
    """
    leetcode solution 2: Space Optimized Binary Search
    Runtime 1160ms Beats 19.33%
    Memory 21.91MB Beats 49.42%
    """

    def repairCars(self, ranks: List[int], cars: int) -> int:
        # The minimum possible time is 1,
        # and the maximum possible time is when the slowest mechanic (highest rank) repairs all cars.
        low, high = 1, cars * cars * ranks[0]

        # Perform binary search to find the minimum time required.
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            # If the total cars repaired is less than required, increase the time.
            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid  # Otherwise, try a smaller time.

        return low


class Solution:
    """
    leetcode solution 3: Using Heap
    Runtime 496ms Beats 58.51%
    Memory 21.62MB Beats 97.36%
    """

    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Count the frequency of each rank using a Counter
        count = Counter(ranks)

        # Create a Min-heap storing [time, rank, n, count]:
        # - time: time for the next repair
        # - rank: mechanic's rank
        # - n: cars repaired by this mechanic
        # - count: number of mechanics with this rank
        # Initial time = rank (as rank * 1^2 = rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)

        # Process until all cars are repaired
        while cars > 0:
            # Pop the mechanic with the smallest current repair time
            time, rank, n, count = heappop(min_heap)

            # Deduct the number of cars repaired by this mechanic group
            cars -= count

            # Increment the number of cars repaired by this mechanic
            n += 1

            # Push the updated repair time back into the heap
            # The new repair time is rank * n^2 (since time increases quadratically with n)
            heappush(min_heap, [rank * n * n, rank, n, count])

        return time
