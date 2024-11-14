"""
Leetcode
2024-11-14
2064. Minimized Maximum of Products Distributed to Any Store
Medium

You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

    A store can only be given at most one product type but can be given any amount of it.
    After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

Return the minimum possible x.

 

Example 1:

Input: n = 6, quantities = [11,6]
Output: 3
Explanation: One optimal way is:
- The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
- The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

Example 2:

Input: n = 7, quantities = [15,10,10]
Output: 5
Explanation: One optimal way is:
- The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
- The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
- The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.

Example 3:

Input: n = 1, quantities = [100000]
Output: 100000
Explanation: The only optimal way is:
- The 100000 products of type 0 are distributed to the only store.
The maximum number of products given to any store is max(100000) = 100000.

 

Constraints:

    m == quantities.length
    1 <= m <= n <= 10^5
    1 <= quantities[i] <= 10^5

Hints:
- There exists a monotonic nature such that when x is smaller than some number, there will be no way to distribute, and when x is not smaller than that number, there will always be a way to distribute.
- If you are given a number k, where the number of products given to any store does not exceed k, could you determine if all products can be distributed?
- Implement a function canDistribute(k), which returns true if you can distribute all products such that any store will not be given more than k products, and returns false if you cannot. Use this function to binary search for the smallest possible k.
"""

import heapq
from math import ceil
from typing import List


class Solution:
    """
    Runtime: 543 ms, faster than 83.26% of Python3 online submissions for Minimized Maximum of Products Distributed to Any Store.
    Memory Usage: 28.8 MB, less than 59.35% of Python3 online submissions for Minimized Maximum of Products Distributed to Any Store.
    """

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def can_distribute(k: int) -> bool:
            return sum(ceil(q / k) for q in quantities) <= n

        lo = 1
        hi = 10**5 + 1

        while lo < hi:
            mid = (lo + hi) // 2
            if can_distribute(mid):
                hi = mid
            else:
                lo = mid + 1

        return hi


class Solution2:
    """
    leetcode solution 2: Greedy + Heap
    Runtime: 5195 ms, faster than 5.43% of Python3 online submissions for Minimized Maximum of Products Distributed to Any Store.
    Memory Usage: 35.1 MB, less than 5.08% of Python3 online submissions for Minimized Maximum of Products Distributed to Any Store.
    """

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)

        # Create a list of tuples (-ratio, quantity, stores_assigned)
        type_store_pairs = [(-q, q, 1) for q in quantities]

        # Use heapq.heapify() to convert the list into a heap in O(m) time
        heapq.heapify(type_store_pairs)

        # Iterate over the remaining n - m stores
        for _ in range(n - m):
            # Pop the element with the maximum ratio (due to negative sign it's min-heap)
            (
                _neg_ratio,
                total_quantity_of_type,
                stores_assigned_to_type,
            ) = heapq.heappop(type_store_pairs)

            # Calculate the new ratio after assigning one more store
            new_stores_assigned_to_type = stores_assigned_to_type + 1
            new_ratio = total_quantity_of_type / new_stores_assigned_to_type

            # Push the updated pair back into the heap
            heapq.heappush(
                type_store_pairs,
                (
                    -new_ratio,
                    total_quantity_of_type,
                    new_stores_assigned_to_type,
                ),
            )

        # Pop the first element to get the final ratio
        _, total_quantity_of_type, stores_assigned_to_type = heapq.heappop(
            type_store_pairs
        )

        # Return the maximum minimum ratio
        return ceil(total_quantity_of_type / stores_assigned_to_type)
