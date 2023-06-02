"""
Leetcode
2101. Detonate the Maximum Bombs (medium)
2023-06-02

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example 1:

Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example 2:

Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

Example 3:

Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.

Constraints:

    1 <= bombs.length <= 100
    bombs[i].length == 3
    1 <= xi, yi, ri <= 105
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    """
    Runtime: 922 ms, faster than 35.75% of Python3 online submissions for Detonate the Maximum Bombs.
    Memory Usage: 17.1 MB, less than 11.50% of Python3 online submissions for Detonate the Maximum Bombs.
    """

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, bomb1 in enumerate(bombs):
            for j in range(i + 1, len(bombs)):
                bomb2 = bombs[j]

                x1, y1, r1 = bomb1
                x2, y2, r2 = bomb2

                distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

                neib1 = graph[(x1, y1, i)]
                if distance <= r1:
                    neib1.append((x2, y2, j))

                neib2 = graph[(x2, y2, j)]
                if distance <= r2:
                    neib2.append((x1, y1, i))

        def bfs(node: (int, int, int)):
            q = [node]
            visited = {node}
            count = 1

            while q:
                cur = q.pop(0)
                for next_node in graph[cur]:
                    if next_node not in visited:
                        count += 1
                        visited.add(next_node)
                        q.append(next_node)

            return count

        nodes = graph.keys()
        return max(bfs(node) for node in nodes) if len(nodes) > 1 else 1


class Solution1:
    """
    leetcode solution: BFS
    Runtime: 819 ms, faster than 58.55% of Python3 online submissions for Detonate the Maximum Bombs.
    Memory Usage: 16.4 MB, less than 55.17% of Python3 online submissions for Detonate the Maximum Bombs.
    """

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)

        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from node i to node j, if bomb i detonates bomb j.
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def bfs(i):
            queue = deque([i])
            visited = set([i])
            while queue:
                cur = queue.popleft()
                for neib in graph[cur]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append(neib)
            return len(visited)

        answer = 0
        for i in range(n):
            answer = max(answer, bfs(i))

        return answer


class Solution2:
    """
    leetcode solution: DFS
    Runtime: 830 ms, faster than 54.11% of Python3 online submissions for Detonate the Maximum Bombs.
    Memory Usage: 17 MB, less than 22.80% of Python3 online submissions for Detonate the Maximum Bombs.
    """

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)

        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from node i to node j, if bomb i detonates bomb j.
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        # DFS to get the number of nodes reachable from a given node cur
        def dfs(cur, visited):
            visited.add(cur)
            for neib in graph[cur]:
                if neib not in visited:
                    dfs(neib, visited)
            return len(visited)

        answer = 0
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))

        return answer


s = Solution()
tests = [
    ([[4, 4, 3], [4, 4, 3]],
     2),

    ([[2, 1, 3], [6, 1, 4]],
     2),

    ([[1, 1, 5], [10, 10, 5]],
     1),

    ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]],
     5),

    ([[1, 1, 1]],
     1),
]
for inp, exp in tests:
    res = s.maximumDetonation(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
