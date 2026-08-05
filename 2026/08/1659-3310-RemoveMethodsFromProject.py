"""
Leetcode
2026-08-05
3310. Remove Methods From Project
Medium

You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

 

Example 1:

Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

Output: [0,1,2,3]

Explanation:

Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.

Example 2:

Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

Output: [3,4]

Explanation:

Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.

Example 3:

Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

Output: []

Explanation:

All methods are suspicious. We can remove them.

 

Constraints:

    1 <= n <= 10^5
    0 <= k <= n - 1
    0 <= invocations.length <= 2 * 10^5
    invocations[i] == [ai, bi]
    0 <= ai, bi <= n - 1
    ai != bi
    invocations[i] != invocations[j]


"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Runtime 352ms Beats 48.48%
    Memory 106.33MB Beats 61.36%
    """

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)

        suspicious = {k}

        q = [k]
        while q:
            nxt_q = []
            for node in q:
                for nxt in graph[node]:
                    if nxt not in suspicious:
                        suspicious.add(nxt)
                        nxt_q.append(nxt)
            q = nxt_q

        all_nodes = list(range(n))
        for node in all_nodes:
            if node in suspicious:
                continue
            for nxt in graph[node]:
                if nxt in suspicious:
                    return all_nodes

        return [node for node in all_nodes if node not in suspicious]


class Solution1:
    """
    leetcode solution: Searching
    Runtime 263ms Beats 78.03%
    Memory 100.91MB Beats 75.76%
    """

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        queue = deque([k])
        suspicious = bytearray(n)
        suspicious[k] = 1

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1

                if suspicious[v] == 0:
                    queue.append(v)
                    suspicious[v] = 1

        can_remove_all = True
        for i in range(n):
            if suspicious[i] == 1 and in_degree[i] > 0:
                can_remove_all = False
                break

        if not can_remove_all:
            return list(range(n))

        return [i for i in range(n) if suspicious[i] == 0]
