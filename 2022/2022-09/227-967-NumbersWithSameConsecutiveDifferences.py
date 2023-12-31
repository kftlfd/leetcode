"""
Leetcode
967. Numbers With Same Consecutive Differences (medium)
2022-09-03

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
"""

from typing import List


# https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution/
# Runtime: 35 ms, faster than 97.96% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 14.3 MB, less than 21.77% of Python3 online submissions for Numbers With Same Consecutive Differences.
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        N, K = n, k

        if N == 1:
            return [i for i in range(10)]

        ans = []

        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)


# https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution/
# Runtime: 47 ms, faster than 87.42% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 14.2 MB, less than 73.81% of Python3 online submissions for Numbers With Same Consecutive Differences.
class Solution1:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        N, K = n, k

        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            # start the next level
            queue = next_queue

        return queue


s = Solution1()
tests = [
    (3, 7),
    (2, 1),
]
for n, k in tests:
    print(n, k)
    print(s.numsSameConsecDiff(n, k))
    print()
