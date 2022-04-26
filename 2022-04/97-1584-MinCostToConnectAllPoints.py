"""
Leetcode
1584. Min Cost to Connect All Points (medium)
2022-04-26

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""



# leetcode solution 1 - Kruskal's Algorithm
# Runtime: 1917 ms, faster than 69.37% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 81.6 MB, less than 69.64% of Python3 online submissions for Min Cost to Connect All Points.
class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.group[i] = i
    
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group
        if group1 == group2:
            return False
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
            
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges = []
        
        # store all edges of complete graph
        for curr_node in range(n):
            for next_node in range(curr_node + 1, n):
                weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))
                
        # sort in increasing order
        all_edges.sort()
        
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return mst_cost



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
