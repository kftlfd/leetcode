"""
Leetcode
2026-10-30
3970. Shortest Path With At Most K Consecutive Identical Characters
Medium

You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

 

Example 1:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

Output: 3

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

    Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.

The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

Example 2:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

Output: 2

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

    Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
    Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.

The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.

Example 3:

Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

Output: -1

Explanation:

There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.

 

Constraints:

    1 <= n == labels.length <= 5 * 10^4
    0 <= edges.length <= 5 * 10^4
    edges[i] == [ui, vi, wi]
    0 <= ui, vi <= n - 1
    ui != vi
    1 <= wi <= 10^4
    labels consists of lowercase English letters
    1 <= k <= 50


Hint 1
The validity of a path depends not only on the current node, but also on how many consecutive times the current node's label has appeared at the end of the path.
Hint 2
Use Dijkstra on states (node, count), where count is the current consecutive run length of labels[node].
Hint 3
When moving from node u to node v, the next count becomes count + 1 if labels[u] == labels[v], otherwise it becomes 1. Ignore transitions where the next count exceeds k.
Hint 4
The answer is the minimum distance among all states ending at node n - 1.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Wrong Answer
    1000 / 1001 testcases passed
    """

    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n < 2:
            return 0

        lb = list(labels)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        q = [(0, 1, 0)]  # (path_weight, consecutive_count, node)
        indegree: list[None | tuple[int, int]] = [None] * n
        indegree[0] = (0, 1)  # min (weight, cnt) seen

        while q:
            weight, cnt, node = heappop(q)
            for neib_node, neib_weight in graph[node]:
                nxt_cnt = cnt + 1 if lb[node] == lb[neib_node] else 1
                nxt_weight = weight + neib_weight
                if nxt_cnt <= k and (indegree[neib_node] is None or indegree[neib_node] > (nxt_weight, nxt_cnt)):
                    indegree[neib_node] = (nxt_weight, nxt_cnt)
                    heappush(q, (nxt_weight, nxt_cnt, neib_node))

        end = indegree[n - 1]
        return -1 if end is None else end[0]


class Solution1:
    """
    leetcode solution: Dijkstra's Algorithm
    Runtime 283ms Beats 76.51%
    Memory 66.05MB Beats 50.60%
    """

    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        # {shortest path length, node index, number of consecutive identical letters at the end}
        pq = []

        dis[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, x, cnt = heappop(pq)

            if d > dis[x][cnt]:
                continue
            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
                if new_cnt > k:
                    continue

                nd = d + w
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(pq, (nd, y, new_cnt))

        return -1
