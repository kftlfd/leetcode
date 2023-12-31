"""
Leetcode
108. Convert Sorted Array to Binary Search Tree (easy)
2022-08-10

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        out = []
        q = [self]
        while q:
            q2 = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node != None:
                    out.append(node.val)
                    q2 += [node.left, node.right]
                else:
                    out.append(None)
            q = q2
        return str(out)


# Runtime: 148 ms, faster than 22.24% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.7 MB, less than 32.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(val=nums[0])
        else:
            mid = len(nums) // 2
            val = nums[mid]
            left = self.sortedArrayToBST(nums[:mid])
            right = self.sortedArrayToBST(nums[mid+1:])
            return TreeNode(val=val, left=left, right=right)


s = Solution()
tests = [
    [-10, -3, 0, 5, 9],
    [1, 3],
]
for t in tests:
    print(t)
    print(s.sortedArrayToBST(t))
    print()
