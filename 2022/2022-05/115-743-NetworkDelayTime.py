"""
Leetcode
743. Network Delay Time (medium)
2022-05-14

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""



# https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions
# Runtime: 632 ms, faster than 44.55% of Python3 online submissions for Network Delay Time.
# Memory Usage: 17 MB, less than 13.69% of Python3 online submissions for Network Delay Time.
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q, t, adj = [(0, k)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == n else -1



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
