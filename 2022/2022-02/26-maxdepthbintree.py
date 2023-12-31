'''
Leetcode
104. Maximum Depth of Binary Tree (easy)
2022-02-14

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Try 1
# breadth-first search
# Runtime: 48 ms, faster than 60.69% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.2 MB, less than 99.17% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        nodes = [root]

        while True:
            tmp = []
            for node in nodes:
                if node != None: 
                    tmp.append(node.left)
                    tmp.append(node.right)
            if tmp:
                depth += 1
                nodes = tmp
            else:
                break
            
        return depth



# modified try1
# Runtime: 48 ms, faster than 60.69% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.4 MB, less than 77.69% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = -1
        nodes = [root]

        while nodes:
            depth += 1
            for node in range(len(nodes) -1, -1, -1):
                if nodes[node] != None:
                    nodes.append(nodes[node].left)
                    nodes.append(nodes[node].right)
                nodes.pop(node)
            
        return depth



# recursion
# Runtime: 40 ms, faster than 89.54% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.3 MB, less than 31.05% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0