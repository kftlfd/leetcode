"""
Leetcode
2026-05-18
1345. Jump Game IV
Hard

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

 

Constraints:

    1 <= arr.length <= 5 * 10^4
    -10^8 <= arr[i] <= 10^8

 
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Runtime 176ms Beats 60.95%
    Memory 33.08MB Beats 88.92%
    """

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return n - 1

        seen = [False] * n
        seen[0] = True

        idxs = defaultdict(list)
        for i, num in enumerate(arr):
            idxs[num].append(i)

        q = deque([0])
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                cur = q.popleft()
                nxt_idxs = [
                    idx
                    for idx in [cur - 1, cur + 1] + idxs[arr[cur]]
                    if not seen[idx] and idx > 0
                ]
                del idxs[arr[cur]]
                for nxt in nxt_idxs:
                    if nxt == n - 1:
                        return steps
                    seen[nxt] = True
                    q.append(nxt)

        return -1


class Solution1:
    """
    leetcode solution 1: Breadth-First Search
    Runtime 179ms Beats 59.10%
    Memory 34.48MB Beats 57.52%
    """

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1


class Solution2:
    """
    leetcode solution 2: Bidirectional BFS
    Runtime 91ms Beats 98.68%
    Memory 32.46MB Beats 99.21%
    """

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1])  # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1
