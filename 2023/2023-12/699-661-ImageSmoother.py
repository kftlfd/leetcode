"""
Leetcode
661. Image Smoother
Easy
2023-12-19

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

 

Example 1:

Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:

Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

 

Constraints:

    m == img.length
    n == img[i].length
    1 <= m, n <= 200
    0 <= img[i][j] <= 255
"""

from typing import List


class Solution:
    """
    Runtime: 481 ms, faster than 64.59% of Python3 online submissions for Image Smoother.
    Memory Usage: 17.1 MB, less than 59.70% of Python3 online submissions for Image Smoother.
    """

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        out = [[0] * n for _ in range(m)]

        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]

        for row in range(m):
            for col in range(n):
                cell_sum = img[row][col]
                cell_count = 1

                for dr, dc in moves:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < m) and (0 <= nc < n):
                        cell_sum += img[nr][nc]
                        cell_count += 1

                out[row][col] = cell_sum // cell_count

        return out


class Solution2:
    """
    leetcode solution 2: Space-Optimized Smoothened Image
    Runtime: 392 ms, faster than 81.96% of Python3 online submissions for Image Smoother.
    Memory Usage: 17.1 MB, less than 59.70% of Python3 online submissions for Image Smoother.
    """

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Create a temp array of size n.
        temp = [0] * n

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the sum and count
                sum = 0
                count = 0

                # Bottom neighbors
                if i + 1 < m:
                    if j - 1 >= 0:
                        sum += img[i + 1][j - 1]
                        count += 1
                    sum += img[i + 1][j]
                    count += 1
                    if j + 1 < n:
                        sum += img[i + 1][j + 1]
                        count += 1

                # Next neighbor
                if j + 1 < n:
                    sum += img[i][j + 1]
                    count += 1

                # This cell
                sum += img[i][j]
                count += 1

                # Previous neighbor
                if j - 1 >= 0:
                    sum += temp[j - 1]
                    count += 1

                # Top neighbors
                if i - 1 >= 0:
                    # Left-top corner-sharing neighbor.
                    if j - 1 >= 0:
                        sum += prev_val
                        count += 1

                    # Top edge-sharing neighbor.
                    sum += temp[j]
                    count += 1

                    # Right-top corner-sharing neighbor.
                    if j + 1 < n:
                        sum += temp[j + 1]
                        count += 1

                # Store the original value of temp[j], which represents
                # original value of img[i - 1][j].
                if i - 1 >= 0:
                    prev_val = temp[j]

                # Save current value of img[i][j] in temp[j].
                temp[j] = img[i][j]

                # Overwrite with smoothed value.
                img[i][j] = sum // count

        # Return the smooth image.
        return img


class Solution3:
    """
    leetcode solution 3: Constant Space Smoothened Image
    Runtime: 512 ms, faster than 38.45% of Python3 online submissions for Image Smoother.
    Memory Usage: 17.1 MB, less than 37.10% of Python3 online submissions for Image Smoother.
    """

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the sum and count
                sum = 0
                count = 0

                # Iterate over all plausible nine indices.
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        # If the indices form valid neighbor
                        if 0 <= x < m and 0 <= y < n:
                            # Extract the original value of img[x][y].
                            sum += img[x][y] % 256
                            count += 1

                # Encode the smoothed value in img[i][j].
                img[i][j] += (sum // count) * 256

        # Extract the smoothed value from encoded img[i][j].
        for i in range(m):
            for j in range(n):
                img[i][j] //= 256

        # Return the smooth image.
        return img


class Solution4:
    """
    leetcode solution 4: Bit Manipulation
    Runtime: 517 ms, faster than 35.41% of Python3 online submissions for Image Smoother.
    Memory Usage: 17.1 MB, less than 59.70% of Python3 online submissions for Image Smoother.
    """

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the sum and count
                sum = 0
                count = 0

                # Iterate over all plausible nine indices.
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        # If the indices form valid neighbor
                        if 0 <= x < m and 0 <= y < n:
                            # Extract the original value of img[x][y].
                            sum += img[x][y] & 255
                            count += 1

                # Encode the smoothed value in img[i][j].
                img[i][j] |= (sum // count) << 8

        # Extract the smoothed value from encoded img[i][j].
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8

        # Return the smooth image.
        return img
