'''
Leetcode
662. Maximum Width of Binary Tree (medium)
2022-02-27

Given the root of a binary tree, return the maximum width 
of the given tree.

The maximum width of a tree is the maximum width among all 
levels.

The width of one level is defined as the length between the 
end-nodes (the leftmost and rightmost non-null nodes), where 
the null nodes between the end-nodes are also counted into 
the length calculation.

It is guaranteed that the answer will in the range of 32-bit 
signed integer.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# try 1
# Time limit exceeded
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: return root
        
        q = [root]
        width = 1
        
        while q:
            
            for i in range(len(q)):
                curr = q.pop(0)
                q.append(curr.left if curr else None)
                q.append(curr.right if curr else None)
                    
            while q and q[0] == None: q.pop(0)
            while q and q[-1] == None: q.pop(-1)
                
            width = max(width, len(q))

        return width
            


# taken from
# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/1803613/Python-3-BFS-and-DFS-Solutions-and-Explanation
# Runtime: 99 ms, faster than 7.14% of Python3 online submissions for Maximum Width of Binary Tree.
# Memory Usage: 14.9 MB, less than 55.95% of Python3 online submissions for Maximum Width of Binary Tree.
class Solution1:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Each index in queue store node and its index in its level
        queue = [(root, 0)]
        maxLength = 1
        while queue:
            nextLevelQueue = []
            # Calculate leftMost and rightMost node
            leftMost, rightMost = queue[0][1], queue[-1][1]
            maxLength = max(maxLength, rightMost - leftMost + 1)
            
            # Append next level's node into new queue
            for currNode, idx in queue:
                # If left, right child exist: append it and its idx
                if currNode.left:
                    nextLevelQueue.append((currNode.left, idx * 2))
                if currNode.right:
                    nextLevelQueue.append((currNode.right, idx * 2 + 1))
            # Replace queue to nextLevelQueue
            queue = nextLevelQueue
        return maxLength