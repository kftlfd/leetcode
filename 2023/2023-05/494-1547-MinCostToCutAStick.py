"""
Leetcode
1547. Minimum Cost to Cut a Stick (hard)
2023-05-28

Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:
0 1 2 3 4 5 6

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

Example 1:
Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).

Example 2:
Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanation: If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Top-down Dynamic Programming
    Runtime: 1786 ms, faster than 29.87% of Python3 online submissions for Minimum Cost to Cut a Stick.
    Memory Usage: 19.7 MB, less than 25.00% of Python3 online submissions for Minimum Cost to Cut a Stick.
    """

    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cuts = [0] + sorted(cuts) + [n]

        def cost(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if right - left == 1:
                return 0
            ans = min(cost(left, mid) + cost(mid, right) +
                      cuts[right] - cuts[left] for mid in range(left + 1, right))
            memo[(left, right)] = ans
            return ans

        return cost(0, len(cuts) - 1)


s = Solution()
tests = [
    ((7, [1, 3, 4, 5]),
     16),

    ((9, [5, 6, 1, 4, 2]),
     22),
]
for inp, exp in tests:
    res = s.minCost(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
