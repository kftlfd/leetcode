"""
Leetcode
2024-09-05
2028. Find Missing Observations
Medium

You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.

 

Constraints:

    m == rolls.length
    1 <= n, m <= 10^5
    1 <= rolls[i], mean <= 6

Hints:
- What should the sum of the n rolls be?
- Could you generate an array of size n such that each element is between 1 and 6?
"""

from typing import List


class Solution:
    """
    Runtime: 1024 ms, faster than 31.28% of Python3 online submissions for Find Missing Observations.
    Memory Usage: 26.7 MB, less than 74.60% of Python3 online submissions for Find Missing Observations.
    """

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_sum = mean * (len(rolls) + n) - sum(rolls)

        if not n <= missing_sum <= 6 * n:
            return []

        out = [1] * n
        out_sum = n
        left = missing_sum - out_sum
        for i, _ in enumerate(out):
            if left == 0:
                break
            cur_add = min(5, left)
            out[i] += cur_add
            left -= cur_add

        return out


class Solution1:
    """
    leetcode solution
    Runtime: 1010 ms, faster than 38.23% of Python3 online submissions for Find Missing Observations.
    Memory Usage: 26.8 MB, less than 57.22% of Python3 online submissions for Find Missing Observations.
    """

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        # Find the remaining sum.
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        # Check if sum is valid or not.
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        # Distribute the remaining mod elements in n_elements list.
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1
        return n_elements
