"""
Leetcode
835. Image Overlap (medium)
2022-10-27

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

Example 1:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.
The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:
Input: img1 = [[0]], img2 = [[0]]
Output: 0
"""

from typing import List, Optional


# leetcode solution 1
# Runtime: 1662 ms, faster than 35.67% of Python3 online submissions for Image Overlap.
# Memory Usage: 14 MB, less than 75.44% of Python3 online submissions for Image Overlap.
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        def shift_and_count(x, y, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count = 0
            right_shift_count = 0
            for r_row, m_row in enumerate(range(y, n)):
                for r_col, m_col in enumerate(range(x, n)):
                    if M[m_row][m_col] == 1 and R[r_row][r_col] == 1:
                        left_shift_count += 1
                    if M[m_row][r_col] == 1 and R[r_row][m_col] == 1:
                        right_shift_count += 1
            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y in range(n):
            for x in range(n):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(
                    max_overlaps, shift_and_count(x, y, img1, img2))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions
                max_overlaps = max(
                    max_overlaps, shift_and_count(x, y, img2, img1))

        return max_overlaps


# leetcode solution 2
# Runtime: 1792 ms, faster than 31.58% of Python3 online submissions for Image Overlap.
# Memory Usage: 14.8 MB, less than 17.54% of Python3 online submissions for Image Overlap.
class Solution1:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        from collections import defaultdict
        n = len(img1)

        def non_zero_cells(M):
            ret = []
            for x in range(n):
                for y in range(n):
                    if M[x][y] == 1:
                        ret.append((x, y))
            return ret

        transformation_count = defaultdict(int)
        max_overlaps = 0

        cells1 = non_zero_cells(img1)
        cells2 = non_zero_cells(img2)

        for x1, y1 in cells1:
            for x2, y2 in cells2:
                vector = (x2-x1, y2-y1)
                transformation_count[vector] += 1
                max_overlaps = max(max_overlaps, transformation_count[vector])

        return max_overlaps


# leetcode solution 3
# Runtime: 793 ms, faster than 69.01% of Python3 online submissions for Image Overlap.
# Memory Usage: 32.2 MB, less than 12.87% of Python3 online submissions for Image Overlap.
class Solution2:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        import numpy as np
        A = np.array(img1)
        B = np.array(img2)
        n = len(img1)

        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, n-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(n*2 - 1):
            for y_shift in range(n*2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+n, y_shift:y_shift+n]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps


s = Solution()
tests = [
    (([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]),
     3),

    (([[1]], [[1]]),
     1),

    (([[0]], [[0]]),
     0),
]
for inp, exp in tests:
    img1, img2 = inp
    res = s.largestOverlap(img1, img2)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
