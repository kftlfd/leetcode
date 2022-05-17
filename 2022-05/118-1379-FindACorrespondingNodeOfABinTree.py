"""
Leetcode
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree (medium)
2022-05-17

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# try 1
# Runtime: 1083 ms, faster than 12.16% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 23.9 MB, less than 68.23% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # find path to target in original tree (preorder traversal)
        path = [] # go_left=0, go_right=1
        def traverse(node, steps):
            if not node:
                return
            elif node == target:
                path[:] = steps
            else:
                traverse(node.left, steps + [0])
                traverse(node.right, steps + [1])
        traverse(original, [])
        
        # go through path on cloned tree
        ans = cloned
        for step in path:
            if step == 0:
                ans = ans.left
            else:
                ans = ans.right
        return ans



# leetcode solution - recursive inorder traversal
# Runtime: 1166 ms, faster than 8.20% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 23.9 MB, less than 68.23% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
class Solution1:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def inorder(og, clone):
            if og:
                inorder(og.left, clone.left)
                if og == target:
                    self.ans = clone
                inorder(og.right, clone.right)
                
        inorder(original, cloned)
        return self.ans



# leetcode solution - iterative inorder traversal
# Runtime: 1091 ms, faster than 11.57% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 24.1 MB, less than 40.41% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
class Solution2:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        stack_o, stack_c = [], []
        node_o, node_c = original, cloned
        
        while stack_o or node_c:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)
                
                node_o = node_o.left
                node_c = node_c.left
                
            node_o = stack_o.pop()
            node_c = stack_c.pop()
            
            if node_o is target:
                return node_c
            
            node_o = node_o.right
            node_c = node_c.right 



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
