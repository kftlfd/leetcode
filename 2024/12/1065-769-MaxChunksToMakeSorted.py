"""
Leetcode
2024-12-19
769. Max Chunks To Make Sorted
Medium

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

 

Constraints:

    n == arr.length
    1 <= n <= 10
    0 <= arr[i] < n
    All the elements of arr are unique.
"""

from collections import deque
from typing import List


class Solution1:
    """
    leetcode solution 1: PrefixMax and SuffixMin Arrays
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Max Chunks To Make Sorted.
    Memory Usage: 17.9 MB, less than 14.45% of Python3 online submissions for Max Chunks To Make Sorted.
    """

    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]

        # Fill the prefix_max array
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])

        # Fill the suffix_min array in reverse order
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])

        chunks = 0
        for i in range(n):
            # A new chunk can be created
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks += 1

        return chunks


class Solution3:
    """
    leetcode solution 3: Monotonic Increasing Stack
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Max Chunks To Make Sorted.
    Memory Usage: 18 MB, less than 14.45% of Python3 online submissions for Max Chunks To Make Sorted.
    """

    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        # Deque to store the maximum elements of each chunk
        stack = deque()

        for i in range(n):
            # Case 1: Current element is larger, starts a new chunk
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                # Case 2: Merge chunks
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)
