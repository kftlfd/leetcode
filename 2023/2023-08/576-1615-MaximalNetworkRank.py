"""
Leetcode
1615. Maximal Network Rank (medium)
2023-08-18

There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Example 2:

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

Constraints:

    2 <= n <= 100
    0 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 2
    0 <= ai, bi <= n-1
    ai != bi
    Each pair of cities has at most one road connecting them.
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 321 ms, faster than 73.62% of Python3 online submissions for Maximal Network Rank.
    Memory Usage: 18 MB, less than 83.19% of Python3 online submissions for Maximal Network Rank.
    """

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j]) - (j in graph[i])
                max_rank = max(max_rank, rank)

        return max_rank


class Solution1:
    """
    https://leetcode.com/problems/maximal-network-rank/discuss/3924675/Beat-100-or-O(V-+-E)-or-Most-Efficient-Solution-or-Greedy:-No-Hash-No-Double-Loop
    Runtime: 272 ms, faster than 100.00% of Python3 online submissions for Maximal Network Rank.
    Memory Usage: 17.8 MB, less than 92.03% of Python3 online submissions for Maximal Network Rank.
    """

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1

        max_degree = 0
        second_max_degree = 0
        for degree in degrees:
            if degree < second_max_degree:
                continue
            second_max_degree = degree
            if second_max_degree > max_degree:
                max_degree, second_max_degree = second_max_degree, max_degree

        is_candidate = [False] * n
        candidate_count = 0
        king = -1
        for i in range(n):
            if degrees[i] == second_max_degree:
                is_candidate[i] = True
                candidate_count += 1
            if degrees[i] == max_degree and max_degree > second_max_degree:
                king = i

        # case 1: multiple candidates with the same max degree
        if max_degree == second_max_degree:
            if candidate_count > max_degree + 1:
                return max_degree * 2

            connection_count = 0
            for a, b in roads:
                if is_candidate[a] and is_candidate[b]:
                    connection_count += 1

            if connection_count < candidate_count * (candidate_count - 1) / 2:
                return max_degree * 2

            return max_degree * 2 - 1

        # case 2: we have a single max degree (king) and multiple second degree candidates
        connection_count = 0
        for a, b in roads:
            if a != king and b != king:
                continue
            if is_candidate[a] or is_candidate[b]:
                connection_count += 1
        if connection_count < candidate_count:
            return max_degree + second_max_degree
        return max_degree + second_max_degree - 1


s = Solution1()
tests = [
    ((4, [[0, 1], [0, 3], [1, 2], [1, 3]]),
     4),

    ((5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]),
     5),

    ((8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]),
     5),
]
for inp, exp in tests:
    res = s.maximalNetworkRank(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
