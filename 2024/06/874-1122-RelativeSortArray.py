"""
Leetcode
1122. Relative Sort Array
Easy
2024-06-11

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

 

Constraints:

    1 <= arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    All the elements of arr2 are distinct.
    Each arr2[i] is in arr1.
"""

from typing import List
from heapq import heappush, heappop


class Solution:
    """
    Runtime: 43 ms, faster than 43.51% of Python3 online submissions for Relative Sort Array.
    Memory Usage: 16.7 MB, less than 67.06% of Python3 online submissions for Relative Sort Array.
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = [0] * len(arr1)
        cnt = {}
        heap = []

        for num in arr2:
            cnt[num] = 0

        for num in arr1:
            if num in cnt:
                cnt[num] += 1
            else:
                heappush(heap, num)

        i = 0
        for num in arr2:
            for _ in range(cnt[num]):
                ans[i] = num
                i += 1

        while heap:
            ans[i] = heappop(heap)
            i += 1

        return ans


class Solution3:
    """
    leetcode solution 3: Using Counting Sort
    Runtime: 37 ms, faster than 79.20% of Python3 online submissions for Relative Sort Array.
    Memory Usage: 16.6 MB, less than 67.06% of Python3 online submissions for Relative Sort Array.
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_element = max(arr1)
        count = [0] * (max_element + 1)

        # Count occurrences of each element
        for element in arr1:
            count[element] += 1

        # Add elements as per relative order
        result = []
        for value in arr2:
            while count[value] > 0:
                result.append(value)
                count[value] -= 1

        # Add remaining elements in ascending order
        for num in range(max_element + 1):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
