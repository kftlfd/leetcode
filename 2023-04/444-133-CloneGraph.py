"""
Leetcode
133. Clone Graph (medium)
2023-04-08

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"( {self.val} -> {[node.val for node in self.neighbors]} )"


class Solution:
    """
    Runtime: 35 ms, faster than 89.00% of Python3 online submissions for Clone Graph.
    Memory Usage: 14.4 MB, less than 17.48% of Python3 online submissions for Clone Graph.
    """

    def cloneGraph(self, node: Node) -> Node:

        if not node:
            return node

        clones = {}

        def get_clone(val: int) -> Node:
            if val not in clones:
                clones[val] = Node(val)
            return clones[val]

        visited = set()
        q = [node]

        while q:
            cur_node = q.pop(0)
            if cur_node.val in visited:
                continue
            node_clone = get_clone(cur_node.val)
            visited.add(cur_node.val)
            for neib in cur_node.neighbors:
                node_clone.neighbors.append(get_clone(neib.val))
                if neib.val not in visited:
                    q.append(neib)

        return clones[node.val]


def build_graph(adj) -> Node:
    nodes = [Node(i) for i in range(len(adj) + 1)]
    for left, right in adj:
        if nodes[right] not in nodes[left].neighbors:
            nodes[left].neighbors.append(nodes[right])
        if nodes[left] not in nodes[right].neighbors:
            nodes[right].neighbors.append(nodes[left])
    return nodes[1]


def graph_to_adj_set(node: Node) -> set:
    adj = set()
    visited = set()
    q = [node]
    while q:
        cur_node = q.pop(0)
        visited.add(cur_node)
        for neib in cur_node.neighbors:
            left, right = sorted([cur_node.val, neib.val])
            adj.add((left, right))
            if neib not in visited:
                q.append(neib)
    return adj


s = Solution()
tests = [
    ([[1, 2], [2, 3], [3, 4], [4, 1]]),
]
for inp in tests:
    root = build_graph(inp)
    copy = s.cloneGraph(root)
    res = graph_to_adj_set(copy)
    exp = graph_to_adj_set(root)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
