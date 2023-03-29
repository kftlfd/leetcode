"""
Leetcode
1402. Reducing Dishes (hard)
2023-03-29

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

Example 2:
Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)

Example 3:
Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.
"""

from typing import List


class Solution:
    """
    leetcode solution 4: Greedy
    Runtime: 48 ms, faster than 53.16% of Python3 online submissions for Reducing Dishes.
    Memory Usage: 13.9 MB, less than 46.84% of Python3 online submissions for Reducing Dishes.
    """

    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction_sorted = sorted(satisfaction)
        max_satisfaction = 0
        suffix_sum = 0

        i = len(satisfaction_sorted) - 1
        while i >= 0 and suffix_sum + satisfaction_sorted[i] > 0:
            suffix_sum += satisfaction_sorted[i]
            max_satisfaction += suffix_sum
            i -= 1

        return max_satisfaction


s = Solution()
tests = [
    ([-1, -8, 0, 5, -9],
     14),

    ([4, 3, 2],
     20),

    ([-1, -4, -5],
     0),
]
for inp, exp in tests:
    res = s.maxSatisfaction(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
