"""
Leetcode
427. Construct Quad Tree (medium)
2023-02-27

Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
    isLeaf: True if the node is leaf node on the tree or False if the node has the four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

    If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
    If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
    Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value
"""

from typing import List
from math import ceil, floor

# Definition for a QuadTree node.


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def toArray(self):
        IS_LEAF = 1
        NOT_LEAF = 0
        arr = []
        q = [self]
        while q:
            node = q.pop(0)
            if not node:
                arr += [None] * 4
            elif node.isLeaf > 0:
                arr += [[IS_LEAF, node.val]]
                q += [None]
            else:
                arr += [[NOT_LEAF, 0]]
                q += [node.topLeft, node.topRight,
                      node.bottomLeft, node.bottomRight]
        end = len(arr)
        while not arr[end - 1]:
            end -= 1
        return arr[:end]


class Solution:
    """
    Runtime: 140 ms, faster than 27.00% of Python3 online submissions for Construct Quad Tree.
    Memory Usage: 14.9 MB, less than 41.32% of Python3 online submissions for Construct Quad Tree.
    """

    def construct(self, grid: List[List[int]]) -> 'Node':

        LEAF = 1
        NOT_LEAF = 0

        def construct_recur(yy: (int, int), xx: (int, int)):
            y1, y2 = yy
            x1, x2 = xx

            if x1 == x2:
                return Node(grid[y1][x1], LEAF, None, None, None, None)

            top_yy = (y1, floor((y1 + y2) / 2))
            bottom_yy = (ceil((y1 + y2) / 2), y2)
            left_xx = (x1, floor((x1 + x2) / 2))
            right_xx = (ceil((x1 + x2) / 2), x2)

            top_left = construct_recur(top_yy, left_xx)
            top_right = construct_recur(top_yy, right_xx)
            bottom_left = construct_recur(bottom_yy, left_xx)
            bottom_right = construct_recur(bottom_yy, right_xx)

            if all(n.isLeaf == 1 for n in [top_left, top_right, bottom_left, bottom_right]) and \
                    all(n.val == top_left.val for n in [top_right, bottom_left, bottom_right]):
                return Node(top_left.val, LEAF, None, None, None, None)

            return Node(0, NOT_LEAF, top_left, top_right, bottom_left, bottom_right)

        n = len(grid) - 1
        return construct_recur((0, n), (0, n))


s = Solution()
tests = [
    ([[1, 1, 0, 0],
      [0, 0, 1, 1],
      [1, 1, 0, 0],
      [0, 0, 1, 1]],
     [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [1, 1], [1, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1]]),

    ([[0, 1],
      [1, 0]],
     [[0, 0], [1, 0], [1, 1], [1, 1], [1, 0]]),

    ([[1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0, 0, 0]],
     [[0, 0], [1, 1], [0, 0], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]])
]


def check_answer(ans_arr, exp_arr):
    for ans_node, exp_node in zip(ans_arr, exp_arr):
        if not exp_node and not ans_node:
            continue
        if not exp_node or not ans_node:
            return False
        if exp_node[0] == 0 and ans_node[0] == 0:
            continue
        if exp_node[1] == ans_node[1]:
            continue
        return False
    return True


for inp, exp in tests:
    res = s.construct(inp).toArray()
    if not check_answer(res, exp):
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
