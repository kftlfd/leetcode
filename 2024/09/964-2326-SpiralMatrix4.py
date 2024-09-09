"""
Leetcode
2024-09-09
2326. Spiral Matrix IV
Medium

You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:

Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:

Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

 

Constraints:

    1 <= m, n <= 10^5
    1 <= m * n <= 10^5
    The number of nodes in the list is in the range [1, m * n].
    0 <= Node.val <= 1000
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 645 ms, faster than 75.07% of Python3 online submissions for Spiral Matrix IV.
    Memory Usage: 54.6 MB, less than 94.93% of Python3 online submissions for Spiral Matrix IV.
    """

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]

        def get_next_coord():
            l, r = 0, n
            t, b = 0, m
            while l < r and t < b:
                for x in range(l, r):
                    yield (t, x)
                for x in range(t + 1, b):
                    yield (x, r - 1)
                for x in range(r - 2, l - 1, -1):
                    yield (b - 1, x)
                for x in range(b - 2, t, -1):
                    yield (x, l)
                l += 1
                t += 1
                r -= 1
                b -= 1

        cur = head
        coords = get_next_coord()
        while cur:
            r, c = coords.send(None)
            ans[r][c] = cur.val
            cur = cur.next

        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 782 ms, faster than 15.07% of Python3 online submissions for Spiral Matrix IV.
    Memory Usage: 56.6 MB, less than 21.59% of Python3 online submissions for Spiral Matrix IV.
    """

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Store the east, south, west, north movements in a matrix.
        i = 0
        j = 0
        cur_d = 0
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = [[-1 for _ in range(n)] for _ in range(m)]

        while head is not None:
            ans[i][j] = head.val
            newi = i + movement[cur_d][0]
            newj = j + movement[cur_d][1]

            # If we bump into an edge or an already filled cell, change the
            # direction.
            if (
                min(newi, newj) < 0
                or newi >= m
                or newj >= n
                or ans[newi][newj] != -1
            ):
                cur_d = (cur_d + 1) % 4
            i += movement[cur_d][0]
            j += movement[cur_d][1]

            head = head.next

        return ans


def create_list(arr: List[int]) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


s = Solution()
tests = [
    ([1, 1, [0]],
     [[0]]),
]
for inp, exp in tests:
    res = s.spiralMatrix(inp[0], inp[1], create_list(inp[2]))
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
