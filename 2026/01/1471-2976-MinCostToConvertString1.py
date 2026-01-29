"""
Leetcode
2026-01-29
2976. Minimum Cost to Convert String I
Medium

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.

Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

 

Constraints:

    1 <= source.length == target.length <= 10^5
    source, target consist of lowercase English letters.
    1 <= cost.length == original.length == changed.length <= 2000
    original[i], changed[i] are lowercase English letters.
    1 <= cost[i] <= 10^6
    original[i] != changed[i]


Hint 1
Construct a graph with each letter as a node, and construct an edge (a, b) with weight c if we can change from character a to letter b with cost c. (Keep the one with the smallest cost in case there are multiple edges between a and b).
Hint 2
Calculate the shortest path for each pair of characters (source[i], target[i]). The sum of cost over all i in the range [0, source.length - 1]. If there is no path between source[i] and target[i], the answer is -1.
Hint 3
Any shortest path algorithms will work since we only have 26 nodes. Since we only have at most 26 * 26 pairs, we can save the result to avoid re-calculation.
Hint 4
We can also use Floyd Warshall's algorithm to precompute all the results.
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Runtime 699ms Beats 68.36%
    Memory 20.90MB Beats 32.49%
    """

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = self.get_min_dists(original, changed, cost)
        ans = 0
        a = ord("a")
        inf = float('inf')
        for x, y in zip(source, target):
            if x == y:
                continue
            u, v = ord(x) - a, ord(y) - a
            if dist[u][v] == inf:
                return -1
            ans += dist[u][v]
        return int(ans)

    def get_min_dists(self, original: List[str], changed: List[str], cost: List[int]) -> List[List[int | float]]:
        # Floyd–Warshall algorithm
        n = 26
        a = ord("a")
        dist = [[float('inf')] * n for _ in range(26)]

        for x, y, w in zip(original, changed, cost):
            u, v = ord(x) - a, ord(y) - a
            if w < dist[u][v]:
                dist[u][v] = w

        for u in range(n):
            dist[u][u] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist


class Solution1:
    """
    leetcode solution 1: Dijkstra's Algorithm
    Runtime 1029ms Beats 50.22%
    Memory 21.70MB Beats 7.17%
    """

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Create a graph representation of character conversions
        adjacency_list = [[] for _ in range(26)]

        # Populate the adjacency list with character conversions
        conversion_count = len(original)
        for i in range(conversion_count):
            adjacency_list[ord(original[i]) - ord("a")].append(
                (ord(changed[i]) - ord("a"), cost[i])
            )

        # Calculate shortest paths for all possible character conversions
        min_conversion_costs = [
            self._dijkstra(i, adjacency_list) for i in range(26)
        ]

        # Calculate the total cost of converting source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                char_conversion_cost = min_conversion_costs[ord(s) - ord("a")][
                    ord(t) - ord("a")
                ]
                if char_conversion_cost == float("inf"):
                    return -1  # Conversion not possible
                total_cost += char_conversion_cost

        return int(total_cost)

    def _dijkstra(
        self, start_char: int, adjacency_list: List[List[tuple]]
    ):
        # Priority queue to store characters with their conversion cost, sorted by cost
        priority_queue = [(0, start_char)]

        # List to store the minimum conversion cost to each character
        min_costs = [float("inf")] * 26

        while priority_queue:
            current_cost, current_char = heappop(priority_queue)

            if min_costs[current_char] != float("inf"):
                continue

            min_costs[current_char] = current_cost

            # Explore all possible conversions from the current character
            for target_char, conversion_cost in adjacency_list[current_char]:
                new_total_cost = current_cost + conversion_cost

                # If we found a cheaper conversion, update its cost
                if min_costs[target_char] == float("inf"):
                    heappush(
                        priority_queue, (new_total_cost, target_char)
                    )

        # Return the list of minimum conversion costs from the starting character to all others
        return min_costs
