"""
Leetcode
2976. Minimum Cost to Convert String I
Medium
2024-07-27

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

    1 <= source.length == target.length <= 105
    source, target consist of lowercase English letters.
    1 <= cost.length == original.length == changed.length <= 2000
    original[i], changed[i] are lowercase English letters.
    1 <= cost[i] <= 106
    original[i] != changed[i]

Hints:
- Construct a graph with each letter as a node, and construct an edge (a, b) with weight c if we can change from character a to letter b with cost c. (Keep the one with the smallest cost in case there are multiple edges between a and b).
- Calculate the shortest path for each pair of characters (source[i], target[i]). The sum of cost over all i in the range [0, source.length - 1]. If there is no path between source[i] and target[i], the answer is -1.
- Any shortest path algorithms will work since we only have 26 nodes. Since we only have at most 26 * 26 pairs, we can save the result to avoid re-calculation.
- We can also use Floyd Warshall's algorithm to precompute all the results.
"""

import heapq
from typing import List


class Solution:
    """
    Runtime: 1253 ms, faster than 72.48% of Python3 online submissions for Minimum Cost to Convert String I.
    Memory Usage: 18.3 MB, less than 61.01% of Python3 online submissions for Minimum Cost to Convert String I.
    """

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def idx(char: str) -> int:
            return ord(char) - 97  # ord('a')

        # Floyd Warshall's algorithm
        graph = [[float('inf')] * 26 for _ in range(26)]

        for u, v, w in zip(original, changed, cost):
            graph[idx(u)][idx(v)] = min(graph[idx(u)][idx(v)], w)

        for i in range(26):
            graph[i][i] = 0

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        ans = 0
        for c1, c2 in zip(source, target):
            cur_cost = graph[idx(c1)][idx(c2)]
            if cur_cost == float('inf'):
                ans = -1
                break
            ans += cur_cost

        return ans


class Solution1:
    """
    leetcode solution 1: Dijkstra's Algorithm
    Runtime: 1380 ms, faster than 66.51% of Python3 online submissions for Minimum Cost to Convert String I.
    Memory Usage: 18.6 MB, less than 15.14% of Python3 online submissions for Minimum Cost to Convert String I.
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

        return total_cost

    def _dijkstra(
        self, start_char: int, adjacency_list: List[List[tuple]]
    ) -> List[int]:
        # Priority queue to store characters with their conversion cost, sorted by cost
        priority_queue = [(0, start_char)]

        # List to store the minimum conversion cost to each character
        min_costs = [float("inf")] * 26

        while priority_queue:
            current_cost, current_char = heapq.heappop(priority_queue)

            if min_costs[current_char] != float("inf"):
                continue

            min_costs[current_char] = current_cost

            # Explore all possible conversions from the current character
            for target_char, conversion_cost in adjacency_list[current_char]:
                new_total_cost = current_cost + conversion_cost

                # If we found a cheaper conversion, update its cost
                if min_costs[target_char] == float("inf"):
                    heapq.heappush(
                        priority_queue, (new_total_cost, target_char)
                    )

        # Return the list of minimum conversion costs from the starting character to all others
        return min_costs


class Solution2:
    """
    leetcode solution 2: Floyd-Warshall Algorithm
    Runtime: 1931 ms, faster than 39.45% of Python3 online submissions for Minimum Cost to Convert String I.
    Memory Usage: 18.2 MB, less than 61.01% of Python3 online submissions for Minimum Cost to Convert String I.
    """

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize result to store the total minimum cost
        total_cost = 0

        # Initialize a 2D list to store the minimum transformation cost
        # between any two characters
        min_cost = [[float("inf")] * 26 for _ in range(26)]

        # Fill the initial transformation costs from the given original,
        # changed, and cost arrays
        for orig, chg, cst in zip(original, changed, cost):
            start_char = ord(orig) - ord("a")
            end_char = ord(chg) - ord("a")
            min_cost[start_char][end_char] = min(
                min_cost[start_char][end_char], cst
            )

        # Use Floyd-Warshall algorithm to find the shortest path between any
        # two characters
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(
                        min_cost[i][j], min_cost[i][k] + min_cost[k][j]
                    )

        # Calculate the total minimum cost to transform the source string to
        # the target string
        for src, tgt in zip(source, target):
            if src == tgt:
                continue
            source_char = ord(src) - ord("a")
            target_char = ord(tgt) - ord("a")

            # If the transformation is not possible, return -1
            if min_cost[source_char][target_char] == float("inf"):
                return -1
            total_cost += min_cost[source_char][target_char]

        return total_cost
