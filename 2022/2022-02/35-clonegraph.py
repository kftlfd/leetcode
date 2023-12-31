'''
Leetcode
133. Clone Graph (medium)
2022-02-23

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



# taken from
# https://leetcode.com/problems/clone-graph/discuss/1792858/Python3-ITERATIVE-BFS-(beats-98)-'less()greater''-Explained
# Runtime: 67 ms, faster than 22.78% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.4 MB, less than 91.72% of Python3 online submissions for Clone Graph.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
                
        from collections import deque
        
        if not node: return node

        q = deque([node])
        cloned_nodes = {node.val: Node(node.val)}
        
        while q:            
        
            curr = q.popleft() # original
            clone = cloned_nodes[curr.val] # clone of original
            
            # append clones of neighbors from original to clone
            for ngbr in curr.neighbors:
                
                if ngbr.val not in cloned_nodes:
                    q.append(ngbr)
                    cloned_nodes[ngbr.val] = Node(ngbr.val)
                
                clone.neighbors.append(cloned_nodes[ngbr.val])
        
        return cloned_nodes[node.val]



tests = [
    [[2,4],[1,3],[2,4],[1,3]],
    [[]],
    []
]