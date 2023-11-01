"""
Leetcode
501. Find Mode in Binary Search Tree (easy)
2023-11-01

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [1,null,2,2]
Output: [2]

Example 2:

Input: root = [0]
Output: [0]

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5

 
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 57 ms, faster than 51.74% of Python3 online submissions for Find Mode in Binary Search Tree.
    Memory Usage: 20.9 MB, less than 9.17% of Python3 online submissions for Find Mode in Binary Search Tree.
    """

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = defaultdict(int)
        max_freq = 0

        def dfs(node):
            nonlocal max_freq

            if not node:
                return

            cnt[node.val] += 1
            max_freq = max(max_freq, cnt[node.val])

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        out = []
        for val, freq in cnt.items():
            if freq == max_freq:
                out.append(val)

        return out


class Solution1:
    """
    leetcode solution 4: no hash-map
    Time: O(n)
    Space: O(n)
    """

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, values):
            if not node:
                return

            # Inorder traversal visits nodes in sorted order
            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

        values = []
        dfs(root, values)

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        for num in values:
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak

            if curr_streak == max_streak:
                ans.append(num)

        return ans


class Solution2:
    """
    leetcode solution 5: no "values" array
    Time: O(n)
    Space: O(n)
    Runtime: 58 ms, faster than 47.28% of Python3 online submissions for Find Mode in Binary Search Tree.
    Memory Usage: 20.3 MB, less than 76.56% of Python3 online submissions for Find Mode in Binary Search Tree.
    """

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                return

            dfs(node.left)

            num = node.val
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak

            if curr_streak == max_streak:
                ans.append(num)

            dfs(node.right)

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        dfs(root)
        return ans


class Solution3:
    """
    leetcode solution 6: true constant space: Morris Traversal
    Time: O(n)
    Space: O(1)
    Runtime: 54 ms, faster than 69.48% of Python3 online submissions for Find Mode in Binary Search Tree.
    Memory Usage: 18.3 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
    """

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        curr = root
        while curr:
            if curr.left:
                # Find the friend
                friend = curr.left
                while friend.right:
                    friend = friend.right

                friend.right = curr

                # Delete the edge after using it
                left = curr.left
                curr.left = None
                curr = left
            else:
                # Handle the current node
                num = curr.val
                if num == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num

                if curr_streak > max_streak:
                    ans = []
                    max_streak = curr_streak

                if curr_streak == max_streak:
                    ans.append(num)

                curr = curr.right

        return ans
