"""
Leetcode
2026-01-23
3510. Minimum Pair Removal to Sort Array II
Hard

Given an array nums, you can perform the following operation any number of times:

    Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
    Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

    The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
    The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].

The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.

 

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9


Hint 1
We can perform the simulation using data structures.
Hint 2
Maintain an array index and value using a map since we need to find the next and previous ones.
Hint 3
Maintain the indices to be removed using a hash set.
Hint 4
Maintain the neighbor sums with the smaller indices (set or priority queue).
Hint 5
Keep the 3 structures in sync during the removals.
"""

import heapq
from typing import List


class Solution:
    """
    leetcode solution: Priority Queue + Lazy Deletion
    Runtime 4903ms Beats 15.89%
    Memory 75.43MB Beats 7.48%
    """

    def minimumPairRemoval(self, nums: List[int]) -> int:
        class Node:
            prev: "Node | None"
            next: "Node | None"

            def __init__(self, value, left):
                self.value = value
                self.left = left
                self.prev = None
                self.next = None

        class PQItem:
            def __init__(self, first, second, cost):
                self.first = first
                self.second = second
                self.cost = cost

            def __lt__(self, other):
                if self.cost == other.cost:
                    return self.first.left < other.first.left
                return self.cost < other.cost

        pq = []
        head = Node(nums[0], 0)
        current = head
        merged = [False] * len(nums)
        decrease_count = 0
        count = 0

        for i in range(1, len(nums)):
            new_node = Node(nums[i], i)
            current.next = new_node
            new_node.prev = current
            heapq.heappush(
                pq, PQItem(current, new_node, current.value + new_node.value)
            )

            if nums[i - 1] > nums[i]:
                decrease_count += 1

            current = new_node

        while decrease_count > 0:
            item = heapq.heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            if (
                merged[first.left]
                or merged[second.left]
                or first.value + second.value != cost
            ):
                continue
            count += 1

            if first.value > second.value:
                decrease_count -= 1

            prev_node = first.prev
            next_node = second.next
            first.next = next_node
            if next_node:
                next_node.prev = first

            if prev_node:
                if prev_node.value > first.value and prev_node.value <= cost:
                    decrease_count -= 1
                elif prev_node.value <= first.value and prev_node.value > cost:
                    decrease_count += 1

                heapq.heappush(
                    pq, PQItem(prev_node, first, prev_node.value + cost)
                )

            if next_node:
                if second.value > next_node.value and cost <= next_node.value:
                    decrease_count -= 1
                elif second.value <= next_node.value and cost > next_node.value:
                    decrease_count += 1
                heapq.heappush(
                    pq, PQItem(first, next_node, cost + next_node.value)
                )

            first.value = cost
            merged[second.left] = True

        return count
