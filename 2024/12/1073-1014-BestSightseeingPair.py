"""
Leetcode
2024-12-27
1014. Best Sightseeing Pair
Medium

You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:

Input: values = [1,2]
Output: 2

 

Constraints:

    2 <= values.length <= 5 * 10^4
    1 <= values[i] <= 1000
"""

from typing import List


class Solution:
    """
    leetcode solution: Dynamic Programming
    """

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        # The left score is initially just the value of the first element.
        max_left_score = values[0]

        max_score = 0

        for i in range(1, n):
            current_right_score = values[i] - i
            # Update the maximum score by combining the best left score so far with the current right score.
            max_score = max(max_score, max_left_score + current_right_score)

            current_left_score = values[i] + i
            # Update the maximum left score up to the current index.
            max_left_score = max(max_left_score, current_left_score)

        return max_score
