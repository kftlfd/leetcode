"""
Leetcode
2025-12-25
3075. Maximize Happiness of Selected Children
Medium

You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

 

Example 1:

Input: happiness = [1,2,3], k = 2
Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.

Example 2:

Input: happiness = [1,1,1,1], k = 2
Output: 1
Explanation: We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.

Example 3:

Input: happiness = [2,3,4,5], k = 1
Output: 5
Explanation: We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.

 

Constraints:

    1 <= n == happiness.length <= 2 * 10^5
    1 <= happiness[i] <= 10^8
    1 <= k <= n

    
Hint 1
Since all the unselected numbers are decreasing at the same rate, we should greedily select k largest values.
Hint 2
The ith largest number (i = 1, 2, 3,…k) should decrease by (i - 1) when it is picked.
Hint 3
Add 0 if the decreased value is negative. 
"""

import heapq
from typing import List


class Solution:
    """
    Runtime 799ms Beats 82.98%
    Memory 43.38MB Beats 95.74%
    """

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        for i, hap in enumerate(sorted(happiness, reverse=True)[:k]):
            cur = hap - i
            if cur <= 0:
                break
            ans += cur
        return ans


class Solution2:
    """
    leetcode solution 2: Max Heap / Priority Queue + Greedy
    Runtime 929ms Beats 12.06%
    Memory 45.73MB Beats 11.35%
    """

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Convert the list into a max heap by inverting the happiness values
        # Python's default heap data structure is a min heap
        max_heap = [-h for h in happiness]
        heapq.heapify(max_heap)

        total_happiness_sum = 0
        turns = 0

        for _ in range(k):
            # Invert again to get the original value
            total_happiness_sum += max(-heapq.heappop(max_heap) - turns, 0)

            # Increment turns for the next iteration
            turns += 1

        return total_happiness_sum
