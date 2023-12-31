"""
Leetcode
1345. Jump Game IV (hard)
2023-03-05

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
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 1477 ms, faster than 13.50% of Python3 online submissions for Jump Game IV.
    Memory Usage: 28.9 MB, less than 68.62% of Python3 online submissions for Jump Game IV.
    """

    def minJumps(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 0

        indexes = defaultdict(list)
        for i, num in enumerate(arr):
            indexes[num].append(i)

        end_index = len(arr) - 1

        visited = set()
        visited.add(0)
        q = [(0, 0)]

        while q:

            curr_index, curr_distance = q.pop(0)

            next_indexes = []
            if curr_index > 0 and curr_index - 1 not in visited:
                next_indexes.append(curr_index - 1)
            if curr_index < end_index and curr_index + 1 not in visited:
                next_indexes.append(curr_index + 1)
            next_indexes += [i for i in indexes[arr[curr_index]]
                             if i not in visited]

            # clear the list to prevent redundant search
            indexes[arr[curr_index]].clear()

            next_distance = curr_distance + 1
            for nxt in next_indexes:
                if nxt == end_index:
                    return next_distance
                visited.add(nxt)
                q.append((nxt, next_distance))

        return 0


class Solution1:
    """
    leetcode solution 2: Bidirectional BFS
    Runtime: 613 ms, faster than 99.35% of Python3 online submissions for Jump Game IV.
    Memory Usage: 27.9 MB, less than 90.57% of Python3 online submissions for Jump Game IV.
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


s = Solution1()
tests = [
    ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404],
     3),

    ([7],
     0),

    ([7, 6, 9, 6, 9, 6, 9, 7],
     1),
]
for inp, exp in tests:
    res = s.minJumps(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
