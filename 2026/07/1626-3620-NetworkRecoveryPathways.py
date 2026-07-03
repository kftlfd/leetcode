"""
Leetcode
2026-07-03
3620. Network Recovery Pathways
Hard

You are given a directed acyclic graph of n nodes numbered from 0 to n-1. This is represented by a 2D array edges of length m, where edges[i] = [ui, vi, costi] indicates a one-way communication from node ui to node vi with a recovery cost of costi.

Some nodes may be offline. You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n-1 are always online.

A path from 0 to n-1 is valid if:

    All intermediate nodes on the path are online.
    The total recovery cost of all edges on the path does not exceed k.

For each valid path, define its score as the minimum edge-cost along that path.

Return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.

 

Example 1:

Input: edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10

Output: 3

Explanation:

    The graph has two possible routes from node 0 to node 3:

        Path 0 → 1 → 3

            Total cost = 5 + 10 = 15, which exceeds k (15 > 10), so this path is invalid.

        Path 0 → 2 → 3

            Total cost = 3 + 4 = 7 <= k, so this path is valid.

            The minimum edge-cost along this path is min(3, 4) = 3.

    There are no other valid paths. Hence, the maximum among all valid path-scores is 3.

Example 2:

Input: edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12

Output: 6

Explanation:

    Node 3 is offline, so any path passing through 3 is invalid.

    Consider the remaining routes from 0 to 4:

        Path 0 → 1 → 4

            Total cost = 7 + 5 = 12 <= k, so this path is valid.

            The minimum edge-cost along this path is min(7, 5) = 5.

        Path 0 → 2 → 3 → 4

            Node 3 is offline, so this path is invalid regardless of cost.

        Path 0 → 2 → 4

            Total cost = 6 + 6 = 12 <= k, so this path is valid.

            The minimum edge-cost along this path is min(6, 6) = 6.

    Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

 

Constraints:

    n == online.length
    2 <= n <= 5 * 10^4
    0 <= m == edges.length <= min(105, n * (n - 1) / 2)
    edges[i] = [ui, vi, costi]
    0 <= ui, vi < n
    ui != vi
    0 <= costi <= 10^9
    0 <= k <= 5 * 10^13
    online[i] is either true or false, and both online[0] and online[n-1] are true.
    The given graph is a directed acyclic graph.


Hint 1
Use binary search on ans.
Hint 2
Check if a particular ans is possible by including only the edges with weights ≥ mid (the current binary-search pivot).
Hint 3
Implement the check function using either Dijkstra or DP (via topological sorting, since the graph is a DAG).
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Wrong answer
    """

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = defaultdict(list)

        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))

        q: list[tuple[int, int | None, int]] = [(0, None, 0)]
        seen: list[int] = [-1] * n
        seen[0] = 0

        while q:
            total_cost, score, node = heappop(q)
            for nxt_node, cost in graph[node]:
                nxt_score = cost if score is None else min(score, cost)
                if total_cost - cost < -k or nxt_score <= seen[nxt_node]:
                    continue
                seen[nxt_node] = nxt_score
                heappush(q, (total_cost - cost, nxt_score, nxt_node))

        return seen[-1]


class Solution1:
    """
    leetcode solution 1: Binary Answer + Shortest Path (Dijkstra)
    Runtime 675ms Beats 78.41%
    Memory 56.91MB Beats 81.82%
    """

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        def check(mid: int) -> bool:
            dis = [float("inf")] * n
            pq = [(0, 0)]
            dis[0] = 0

            while pq:
                d, u = heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True
                if d > dis[u]:
                    continue

                for v, w in g[u]:
                    if w < mid:
                        continue
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heappush(pq, (dis[v], v))
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r


class Solution2:
    """
    leetcode solution 2: Binary Answer + Memoization Search
    Runtime 643ms Beats 87.50%
    Memory 90.78MB Beats 5.68%
    """

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        def check(mid: int) -> bool:
            memo = [-1] * n

            def dfs(u: int) -> int:
                if u == n - 1:
                    return 0
                if memo[u] != -1:
                    return memo[u]

                res = float("inf")
                for v, w in g[u]:
                    if w >= mid:
                        res = min(res, dfs(v) + w)

                memo[u] = res
                return res

            return dfs(0) <= k

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r


class Solution3:
    """
    leetcode solution 3: Binary Answer + Topological Sorting + Dynamic Programming
    Runtime 574ms Beats 98.86%
    Memory 60.74MB Beats 29.55%
    """

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        deg = [0] * n
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            deg[v] += 1
            l = min(l, w)
            r = max(r, w)

        # Delete unreachable nodes
        q = deque([i for i in range(1, n) if deg[i] == 0])
        while q:
            u = q.popleft()
            for v, _ in g[u]:
                deg[v] -= 1
                if v and deg[v] == 0:
                    q.append(v)

        def check(mid: int) -> bool:
            dp = [math.inf] * n
            cdeg = deg.copy()
            dp[0] = 0

            q = deque([0])
            while q:
                u = q.popleft()
                if u == n - 1:
                    return dp[u] <= k

                for v, w in g[u]:
                    if w >= mid:
                        dp[v] = min(dp[v], dp[u] + w)
                    cdeg[v] -= 1
                    if cdeg[v] == 0:
                        q.append(v)
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
