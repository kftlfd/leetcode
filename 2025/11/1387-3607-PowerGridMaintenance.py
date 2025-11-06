"""
Leetcode
2025-11-06
3607. Power Grid Maintenance
Medium

You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

    [1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

    [2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

Example 1:

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:

    Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
    Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
    Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
    Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
    Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
    Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.

Example 2:

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:

    There are no connections, so each station is its own isolated grid.
    Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
    Query [2,1]: Station 1 goes offline.
    Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.

 

Constraints:

    1 <= c <= 10^5
    0 <= n == connections.length <= min(105, c * (c - 1) / 2)
    connections[i].length == 2
    1 <= ui, vi <= c
    ui != vi
    1 <= queries.length <= 2 * 10^5
    queries[i].length == 2
    queries[i][0] is either 1 or 2.
    1 <= queries[i][1] <= c


"""

from collections import defaultdict
import heapq
from typing import Dict, List

from sortedcontainers import SortedSet


class Solution:
    """
    Runtime 4110ms Beats 5.15%
    Memory 223.15MB Beats 5.15%
    """

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        stations = self.Stations(c, connections)
        ans = []

        for query_type, station in queries:
            if query_type == 1:
                ans.append(stations.check(station))
            else:
                stations.disconnect(station)

        return ans

    class Stations:
        def __init__(self, n: int, connections: List[List[int]]) -> None:
            self.n = n
            self.grids = {}
            self.grid_root = {}
            self.grid_online = defaultdict(SortedSet)

            for i in range(1, n + 1):
                self.grids[i] = i

            def find_root(x: int):
                r = self.grids[x]
                while r != self.grids[r]:
                    r = self.grids[r]
                return r

            def union(x: int, y: int):
                rx = find_root(x)
                ry = find_root(y)
                self.grids[ry] = rx
                self.grids[y] = rx

            for x, y in connections:
                union(x, y)

            for i in range(1, n + 1):
                ri = find_root(i)
                self.grid_online[ri].add(i)

            for i in range(1, n + 1):
                root = self.grids[i]
                while self.grids[root] != root:
                    root = self.grids[root]
                self.grid_root[i] = root

        def check(self, station: int) -> int:
            online_set = self.grid_online[self.grid_root[station]]
            if not online_set:
                return -1
            if station in online_set:
                return station
            min_val = online_set[0]
            if not isinstance(min_val, int):
                raise ValueError('non-int value in grid set')
            return min_val

        def disconnect(self, station: int) -> None:
            online_set = self.grid_online[self.grid_root[station]]
            online_set.discard(station)


class Solution1:
    """
    leetcode solution 1: Union-Find + Reverse Processing Query
    Runtime 391ms Beats 48.53%
    Memory 107.91MB Beats 54.66%
    """

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = self.DSU(c + 1)
        for p in connections:
            dsu.join(p[0], p[1])

        online = [True] * (c + 1)
        offline_counts = [0] * (c + 1)
        minimum_online_stations = {}

        for q in queries:
            op, x = q[0], q[1]
            if op == 2:
                online[x] = False
                offline_counts[x] += 1

        for i in range(1, c + 1):
            root = dsu.find(i)
            if root not in minimum_online_stations:
                minimum_online_stations[root] = -1

            station = minimum_online_stations[root]
            if online[i]:
                if station == -1 or station > i:
                    minimum_online_stations[root] = i

        ans = []
        for i in range(len(queries) - 1, -1, -1):
            op, x = queries[i][0], queries[i][1]
            root = dsu.find(x)
            station = minimum_online_stations[root]

            if op == 1:
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(station)

            if op == 2:
                if offline_counts[x] > 1:
                    offline_counts[x] -= 1
                else:
                    online[x] = True
                    if station == -1 or station > x:
                        minimum_online_stations[root] = x

        return ans[::-1]

    class DSU:
        def __init__(self, size):
            self.parent = list(range(size))

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def join(self, u, v):
            self.parent[self.find(v)] = self.find(u)


class Vertex:
    def __init__(self, vertex_id: int = None):
        self.vertex_id = vertex_id
        self.offline = False
        self.power_grid_id = -1
        if vertex_id is not None:
            self.vertex_id = vertex_id


class Graph:
    def __init__(self):
        self.adj: Dict[int, List[int]] = {}
        self.vertices: Dict[int, Vertex] = {}

    def add_vertex(self, id: int, value: Vertex):
        self.vertices[id] = value
        self.adj[id] = []

    def add_edge(self, u: int, v: int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def get_vertex_value(self, id: int) -> Vertex:
        return self.vertices[id]

    def get_connected_vertices(self, id: int) -> List[int]:
        return self.adj[id]


class Solution2:
    """
    leetcode solution 2: DFS/BFS + Priority Queue
    Runtime 1072ms Beats 11.76%
    Memory 140.28MB Beats 6.13%
    """

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = Graph()
        for i in range(c):
            v = Vertex(i + 1)
            graph.add_vertex(i + 1, v)

        for conn in connections:
            graph.add_edge(conn[0], conn[1])

        power_grids = []
        power_grid_id = 0

        for i in range(1, c + 1):
            v = graph.get_vertex_value(i)
            if v.power_grid_id == -1:
                power_grid = []
                self.traverse(v, power_grid_id, power_grid, graph)
                power_grids.append(power_grid)
                power_grid_id += 1

        ans = []
        for q in queries:
            op, x = q[0], q[1]
            if op == 1:
                vertex = graph.get_vertex_value(x)
                if not vertex.offline:
                    ans.append(x)
                else:
                    power_grid = power_grids[vertex.power_grid_id]
                    while (
                        power_grid
                        and graph.get_vertex_value(power_grid[0]).offline
                    ):
                        heapq.heappop(power_grid)
                    ans.append(power_grid[0] if power_grid else -1)
            elif op == 2:
                graph.get_vertex_value(x).offline = True

        return ans

    def traverse(
        self, u: Vertex, power_grid_id: int, power_grid: List[int], graph: Graph
    ):
        u.power_grid_id = power_grid_id
        heapq.heappush(power_grid, u.vertex_id)
        for vid in graph.get_connected_vertices(u.vertex_id):
            v = graph.get_vertex_value(vid)
            if v.power_grid_id == -1:
                self.traverse(v, power_grid_id, power_grid, graph)
