"""
Leetcode
373. Find K Pairs with Smallest Sums (medium)
2023-06-27

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:

    1 <= nums1.length, nums2.length <= 10^5
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1 and nums2 both are sorted in ascending order.
    1 <= k <= 10^4
"""

from typing import List
import heapq


class Solution:
    """
    leetcode solution
    Time: O(min(k*log(k), m*n*log(m*n))) -- m = len(nums1), n = len(nums2)
    Space: O(min(k, m*n))
    Runtime: 1108 ms, faster than 76.65% of Python3 online submissions for Find K Pairs with Smallest Sums.
    Memory Usage: 36.5 MB, less than 34.91% of Python3 online submissions for Find K Pairs with Smallest Sums.
    """

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        pairs = []
        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited = {(0, 0)}

        while k > 0 and min_heap:
            val, (i, j) = heapq.heappop(min_heap)
            pairs.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))

            k -= 1

        return pairs


s = Solution()
tests = [
    (([1, 7, 11], [2, 4, 6], 3),
     [[1, 2], [1, 4], [1, 6]]),

    (([1, 1, 2], [1, 2, 3], 2),
     [[1, 1], [1, 1]]),

    (([1, 2], [3], 3),
     [[1, 3], [2, 3]]),
]
for inp, exp in tests:
    res = s.kSmallestPairs(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
