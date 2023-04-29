"""
Leetcode
1697. Checking Existence of Edge Length Limited Paths (hard)
2023-04-29

An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

Example 1:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.

Example 2:
Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.
"""

from typing import List
from collections import defaultdict
from math import inf


class Solution1:
    """
    Time Limit Exceeded
    """

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(dict)

        for u, v, dis in edgeList:
            min_dist = min(graph[u].get(v, inf), dis)
            graph[u][v] = min_dist
            graph[v][u] = min_dist

        ans = []

        for p, q, limit in queries:
            visited = set()
            queue = list(graph[p].items())
            saved_answer = False

            while queue:
                node, dis = queue.pop(0)
                if dis >= limit:
                    continue
                if node == q:
                    ans.append(True)
                    saved_answer = True
                    break
                visited.add(node)
                queue += [pair for pair in graph[node].items() if pair[0]
                          not in visited]

            if not saved_answer:
                ans.append(False)

        return ans


class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int):
        group1 = self.find(node1)
        group2 = self.find(node2)

        if group1 == group2:
            return

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)


class Solution2:
    """
    leetcode solution
    Runtime: 1895 ms, faster than 83.65% of Python3 online submissions for Checking Existence of Edge Length Limited Paths.
    Memory Usage: 64.1 MB, less than 7.55% of Python3 online submissions for Checking Existence of Edge Length Limited Paths.
    """

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        uf = UnionFind(n)
        queries_count = len(queries)
        ans = [False] * queries_count

        # Store original indices with all queries.
        queries_with_index = [[] for _ in range(queries_count)]
        for i in range(queries_count):
            queries_with_index[i] = queries[i]
            queries_with_index[i].append(i)

        # Sort all edges in increasing order of their edge weights.
        edgeList.sort(key=lambda x: x[2])
        # Sort all queries in increasing order of the limit of edge allowed.
        queries_with_index.sort(key=lambda x: x[2])

        edges_index = 0

        # Iterate on each query one by one.
        for [p, q, limit, query_original_index] in queries_with_index:
            # We can attach all edges which satisfy the limit given by the query.
            while edges_index < len(edgeList) and edgeList[edges_index][2] < limit:
                node1 = edgeList[edges_index][0]
                node2 = edgeList[edges_index][1]
                uf.join(node1, node2)
                edges_index += 1

            ans[query_original_index] = uf.are_connected(p, q)

        return ans


s = Solution2()
tests = [
    ((3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]),
     [False, True]),

    ((5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]),
     [True, False]),
]
for inp, exp in tests:
    res = s.distanceLimitedPathsExist(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
