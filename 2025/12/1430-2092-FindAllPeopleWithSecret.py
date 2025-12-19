"""
Leetcode
2025-12-19
2092. Find All People With Secret
Hard

You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.

 

Example 1:

Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
Output: [0,1,2,3,5]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.

Example 2:

Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
Output: [0,1,3]
Explanation:
At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.

Example 3:

Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
Output: [0,1,2,3,4]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
Note that person 2 can share the secret at the same time as receiving it.
At time 2, person 3 shares the secret with person 4.
Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.

 

Constraints:

    2 <= n <= 10^5
    1 <= meetings.length <= 10^5
    meetings[i].length == 3
    0 <= xi, yi <= n - 1
    xi != yi
    1 <= timei <= 10^5
    1 <= firstPerson <= n - 1


Hint 1
Could you model all the meetings happening at the same time as a graph?
Hint 2
What data structure can you use to efficiently share the secret?
Hint 3
You can use the union-find data structure to quickly determine who knows the secret and share the secret.
"""

from collections import defaultdict, deque
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    """
    Runtime 5108ms Beats 5.10%
    Memory 55.26MB Beats 82.17%
    """

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knowsSecret = [False] * n
        knowsSecret[0] = True
        knowsSecret[firstPerson] = True

        byTime = defaultdict(list)
        for x, y, t in meetings:
            byTime[t].append((x, y))

        for _, meets in sorted(byTime.items()):
            changes = True
            while changes:
                changes = False
                for x, y in meets:
                    xKnows = knowsSecret[x]
                    yKnows = knowsSecret[y]
                    if xKnows and not yKnows:
                        knowsSecret[y] = True
                        changes = True
                    if yKnows and not xKnows:
                        knowsSecret[x] = True
                        changes = True

        return [i for i, knows in enumerate(knowsSecret) if knows]


class Solution1:
    """
    leetcode solution 1: Breadth First Search
    Time Limit Exceeded
    """

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new information,
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Queue for BFS. It will store (person, time of knowing the secret)
        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        # Do BFS
        while q:
            person, time = q.popleft()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    q.append((next_person, t))

        # Since we visited only those people who know the secret,
        # we need to return indices of all visited people.
        return [i for i in range(n) if earliest[i] != inf]


class Solution2:
    """
    leetcode solution 2: Depth First Search
    Time Limit Exceeded
    """

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new information,
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Stack for DFS. It will store (person, time of knowing the secret)
        stack = [(0, 0), (firstPerson, 0)]

        # Do DFS
        while stack:
            person, time = stack.pop()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    stack.append((next_person, t))

        # Since we visited only those people who know the secret
        # we need to return indices of all visited people.
        return [i for i in range(n) if earliest[i] != inf]


class Solution3:
    """
    leetcode solution 3: Earliest Informed First Traversal
    Runtime 405ms Beats 28.03%
    Memory 68.72MB Beats 40.77%
    """

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Priority Queue for BFS. It stores (time secret learned, person)
        # It pops the person with the minimum time of knowing the secret.
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))

        # Visited array to mark if a person is visited or not.
        # We will mark a person as visited after it is dequeued
        # from the queue.
        visited = [False] * n

        # Do BFS, but pop minimum.
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True
            for t, next_person in graph[person]:
                if not visited[next_person] and t >= time:
                    heappush(pq, (t, next_person))

        # Since we visited only those people who know the secret
        # we need to return indices of all visited people.
        return [i for i in range(n) if visited[i]]


class Solution4:
    """
    leetcode solution 4: Breadth First Search on Time Scale
    Runtime 373ms Beats 38.22%
    Memory 61.52MB Beats 68.15%
    """

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort meetings in increasing order of time
        meetings.sort(key=lambda x: x[2])

        # Group Meetings in increasing order of time
        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        # Boolean Array to mark if a person knows the secret or not
        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True

        # Process in increasing order of time
        for t in same_time_meetings:
            # For each person, save all the people whom he/she meets at time t
            meet = defaultdict(list)
            for x, y in same_time_meetings[t]:
                meet[x].append(y)
                meet[y].append(x)

            # Start traversal from those who already know the secret at time t
            # Set to avoid redundancy
            q = set()
            for x, y in same_time_meetings[t]:
                if knows_secret[x]:
                    q.add(x)
                if knows_secret[y]:
                    q.add(y)

            # Do BFS
            q = deque(q)
            while q:
                person = q.popleft()
                for next_person in meet[person]:
                    if not knows_secret[next_person]:
                        knows_secret[next_person] = True
                        q.append(next_person)

        # List of people who know the secret
        return [i for i in range(n) if knows_secret[i]]


class Solution5:
    """
    leetcode solution 5: Union-Find with Reset
    Runtime 488ms Beats 19.11%
    Memory 54.47MB Beats 84.71%
    """

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort meetings in increasing order of time
        meetings.sort(key=lambda x: x[2])

        # Group Meetings in increasing order of time
        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        # Create graph
        graph = self.UnionFind(n)
        graph.unite(firstPerson, 0)

        # Process in increasing order of time
        for t in same_time_meetings:
            # Unite two persons taking part in a meeting
            for x, y in same_time_meetings[t]:
                graph.unite(x, y)

            # If any one knows the secret, both will be connected to 0.
            # If no one knows the secret, then reset.
            for x, y in same_time_meetings[t]:
                if not graph.connected(x, 0):
                    # No need to check for y since x and y were united
                    graph.reset(x)
                    graph.reset(y)

        # Al those who are connected to 0 will know the secret
        return [i for i in range(n) if graph.connected(i, 0)]

    class UnionFind:
        def __init__(self, nodes: int):
            # Initialize parent and rank arrays
            self.parent = [i for i in range(nodes)]
            self.rank = [0] * nodes

        def find(self, x: int) -> int:
            # Find the parent of node x. Use Path Compression
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def unite(self, x: int, y: int) -> None:
            # Unite two nodes x and y, if they are not already united
            px = self.find(x)
            py = self.find(y)
            if px != py:
                # Union by Rank Heuristic
                if self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                elif self.rank[px] < self.rank[py]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px] += 1

        def connected(self, x: int, y: int) -> bool:
            # Check if two nodes x and y are connected or not
            return self.find(x) == self.find(y)

        def reset(self, x: int) -> None:
            # Reset the initial properties of node x
            self.parent[x] = x
            self.rank[x] = 0
