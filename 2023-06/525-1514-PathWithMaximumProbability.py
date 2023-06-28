"""
Leetcode
1514. Path with Maximum Probability (medium)
2023-06-28

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:

    2 <= n <= 10^4
    0 <= start, end < n
    start != end
    0 <= a, b < n
    a != b
    0 <= succProb.length == edges.length <= 2*10^4
    0 <= succProb[i] <= 1
    There is at most one edge between every two nodes.
"""

from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    """
    leetcode solution 1: Bellman-Ford Algorithm
    Time: O(n*m) -- n = number of nodes, m = number of edges
    Space: O(n)
    Runtime: 786 ms, faster than 22.02% of Python3 online submissions for Path with Maximum Probability.
    Memory Usage: 27.8 MB, less than 97.42% of Python3 online submissions for Path with Maximum Probability.
    """

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        max_prob = [0] * n
        max_prob[start] = 1

        for _ in range(n - 1):
            # if there is no larger probability found during a roud of updates,
            # stop the update process
            has_update = False
            for edge, path_prob in zip(edges, succProb):
                u, v = edge
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = True
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = True
            if not has_update:
                break

        return max_prob[end]


class Solution1:
    """
    leetcode solution 2: Shortest Path Faster Algorithm
    Time: O(n*m) -- n = number of nodes, m = number of edges
    Space: O(n+m)
    Runtime: 698 ms, faster than 76.52% of Python3 online submissions for Path with Maximum Probability.
    Memory Usage: 29.4 MB, less than 17.08% of Python3 online submissions for Path with Maximum Probability.
    """

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        q = deque([start])
        while q:
            cur_node = q.popleft()
            for nxt_node, path_prob in graph[cur_node]:
                # Only update max_prob[nxt_node] if the current path
                # increases the probability of reach nxt_node
                cur_prob = max_prob[cur_node] * path_prob
                if cur_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = cur_prob
                    q.append(nxt_node)

        return max_prob[end]


class Solution2:
    """
    leetcode solution 3: Dijkstra's Algorithm
    n = number of nodes, m = number of edges
    Time: O(m + n*log(n)) when a Fibonacci heap is used, or O(n + m*log(n))) for a Binary heap.
    Space: O(n+m)
    Runtime: 674 ms, faster than 92.58% of Python3 online submissions for Path with Maximum Probability.
    Memory Usage: 29.2 MB, less than 24.94% of Python3 online submissions for Path with Maximum Probability.
    """

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        pq = [(-1.0, start)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)

            if cur_node == end:
                return -cur_prob

            for nxt_node, path_prob in graph[cur_node]:
                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))

        return 0.0


s = Solution2()
tests = [
    ((3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
     0.25),

    ((3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),
     0.3),

    ((3, [[0, 1]], [0.5], 0, 2),
     0.0),
]
for inp, exp in tests:
    res = s.maxProbability(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
