"""
Leetcode
956. Tallest Billboard (hard)
2023-06-24

You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.

Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.

Constraints:

    1 <= rods.length <= 20
    1 <= rods[i] <= 1000
    sum(rods[i]) <= 5000
"""

from typing import List


class Solution:
    """
    leetcode solution 1: meet in the middle
    Time, Space: O(3^(n/2))
    Runtime: 781 ms, faster than 43.75% of Python3 online submissions for Tallest Billboard.
    Memory Usage: 27.2 MB, less than 29.17% of Python3 online submissions for Tallest Billboard.
    """

    def tallestBillboard(self, rods: List[int]) -> int:

        # helper function to collect every combination "(left, right)"
        def get_combinations(half_rods):
            states = set()
            states.add((0, 0))
            for r in half_rods:
                new_states = set()
                for left, right in states:
                    new_states.add((left + r, right))
                    new_states.add((left, right + r))
                states |= new_states

            dp = {}
            for left, right in states:
                dp[left - right] = max(dp.get(left - right, 0), left)
            return dp

        n = len(rods)
        first_half = get_combinations(rods[:n//2])
        second_half = get_combinations(rods[n//2:])

        ans = 0
        for diff in first_half:
            if -diff in second_half:
                ans = max(ans, first_half[diff] + second_half[-diff])

        return ans


class Solution1:
    """
    leetcode solution 2: Dynamic Programming
    Time: O(n*m) -- n = len(rods), m = max sum of rods
    Space: O(m)
    Runtime: 570 ms, faster than 64.58% of Python3 online submissions for Tallest Billboard.
    Memory Usage: 17 MB, less than 52.08% of Python3 online submissions for Tallest Billboard.
    """

    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[taller - shorter] = taller
        dp = {0: 0}

        for r in rods:
            # dp.copy() means we don't add r to these stands.
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff

                # add r to the taller stand, thus the height difference is increased to diff + r
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)

                # add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller)
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)

            dp = new_dp

        # return the maximum height with 0 difference
        return dp.get(0, 0)


s = Solution1()
tests = [
    ([1, 2, 3, 6],
     6),

    ([1, 2, 3, 4, 5, 6],
     10),

    ([1, 2],
     0),
]
for inp, exp in tests:
    res = s.tallestBillboard(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
