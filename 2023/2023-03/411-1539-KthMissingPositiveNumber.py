"""
Leetcode
1539. Kth Missing Positive Number (easy)
2023-03-06

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

from typing import List


class Solution:
    """
    Runtime: 50 ms, faster than 83.51% of Python3 online submissions for Kth Missing Positive Number.
    Memory Usage: 13.9 MB, less than 80.43% of Python3 online submissions for Kth Missing Positive Number.
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:

        curr_int = 0

        for num in arr:

            curr_int += 1

            if num == curr_int:
                continue

            diff = num - curr_int
            if diff > k - 1:
                return curr_int + k - 1

            curr_int += diff
            k -= diff

        return curr_int + k


s = Solution()
tests = [
    (([2, 3, 4, 7, 11], 5),
     9),

    (([1, 2, 3, 4], 2),
     6),

    (([8, 17, 23, 34, 37, 42], 16),
     18)
]
for inp, exp in tests:
    res = s.findKthPositive(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
