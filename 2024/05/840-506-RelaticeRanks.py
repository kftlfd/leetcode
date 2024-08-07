"""
Leetcode
506. Relative Ranks
Easy
2024-05-08

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

 

Constraints:

    n == score.length
    1 <= n <= 10^4
    0 <= score[i] <= 10^6
    All the values in score are unique.
"""

import heapq
from typing import List


class Solution:
    """
    Runtime: 70 ms, faster than 40.61% of Python3 online submissions for Relative Ranks.
    Memory Usage: 17.6 MB, less than 71.46% of Python3 online submissions for Relative Ranks.   
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = {score: place for place, score in enumerate(
            sorted(score, reverse=True))}
        return [self.getRank(ranks[s]) for s in score]

    def getRank(self, place: int) -> str:
        if place == 0:
            return "Gold Medal"
        if place == 1:
            return "Silver Medal"
        if place == 2:
            return "Bronze Medal"
        return f"{place+1}"


class Solution2:
    """
    leetcode solution 2: Heap (Priority Queue)
    Runtime: 57 ms, faster than 91.08% of Python3 online submissions for Relative Ranks.
    Memory Usage: 17.9 MB, less than 22.65% of Python3 online submissions for Relative Ranks.
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        # Create a heap of pairs (score, index)
        heap = []
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))

        # Assign ranks to athletes
        rank = [0] * N
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place += 1

        return rank


class Solution3:
    """
    leetcode solution 3: Array as Map
    Runtime: 69 ms, faster than 43.40% of Python3 online submissions for Relative Ranks.
    Memory Usage: 18 MB, less than 22.65% of Python3 online submissions for Relative Ranks.
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        # Add the original index of each score to the array
        # Where the score is the key
        M = max(score)
        score_to_index = [0] * (M + 1)
        for i in range(N):
            score_to_index[score[i]] = i + 1

        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        # Assign ranks to athletes
        rank = [None] * N
        place = 1
        for i in range(M, -1, -1):
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place < 4:
                    rank[original_index] = MEDALS[place - 1]
                else:
                    rank[original_index] = str(place)
                place += 1
        return rank
