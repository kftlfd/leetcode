"""
Leetcode
2389. Longest Subsequence With Limited Sum (easy)
2022-12-25

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

Example 2:
Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0
"""

from typing import List, Optional
from bisect import bisect_right


# Runtime: 107 ms, faster than 94.17% of Python3 online submissions for Longest Subsequence With Limited Sum.
# Memory Usage: 14.1 MB, less than 79.61% of Python3 online submissions for Longest Subsequence With Limited Sum.
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        prefix_sums = []
        curr_sum = 0
        for n in sorted(nums):
            curr_sum += n
            prefix_sums.append(curr_sum)

        n = len(nums) - 1

        def bin_search(val):
            """return index in prefix_sums of sum that is <= val"""
            l = 0
            r = n
            mid = 0
            while l <= r:
                mid = (l + r) // 2
                num = prefix_sums[mid]
                if num == val:
                    return mid + 1
                elif num > val:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        return list(map(bin_search, queries))


# Runtime: 92 ms, faster than 99.90% of Python3 online submissions for Longest Subsequence With Limited Sum.
# Memory Usage: 14.3 MB, less than 40.29% of Python3 online submissions for Longest Subsequence With Limited Sum.
class Solution1:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        prefix_sums = []
        curr_sum = 0
        for n in sorted(nums):
            curr_sum += n
            prefix_sums.append(curr_sum)

        return list(map(lambda x: bisect_right(prefix_sums, x), queries))


s = Solution1()
tests = [
    (([4, 5, 2, 1], [3, 10, 21]),
     [2, 3, 4]),

    (([2, 3, 4, 5], [1]),
     [0])
]
for inp, exp in tests:
    nums, queries = inp
    res = s.answerQueries(nums, queries)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
