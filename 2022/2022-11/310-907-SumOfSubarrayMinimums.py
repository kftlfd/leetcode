"""
Leetcode
907. Sum of Subarray Minimums (medium)
2022-11-25

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
"""

from typing import List, Optional


# leetcode - Approach 1: Monotonic Stack - Contribution of Each Element
# Runtime: 1438 ms, faster than 22.83% of Python3 online submissions for Sum of Subarray Minimums.
# Memory Usage: 18.8 MB, less than 60.96% of Python3 online submissions for Sum of Subarray Minimums.
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0

        for i in range(len(arr) + 1):

            # when i reaches the array length, it is an indication that
            # all the elements have been processed, and the remaining
            # elements in the stack should now be popped out.

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):

                # Notice the sign ">=", This ensures that no contribution
                # is counted twice. right_boundary takes equal or smaller
                # elements into account while left_boundary takes only the
                # strictly smaller elements into account

                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(i)

        return sum_of_minimums % MOD


# leetcode - Approach 2: Monotonic Stack + Dynamic Programming
# Runtime: 1287 ms, faster than 37.74% of Python3 online submissions for Sum of Subarray Minimums.
# Memory Usage: 18.9 MB, less than 34.26% of Python3 online submissions for Sum of Subarray Minimums.
class Solution1:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # monotonic increasing stack
        stack = []

        # make a dp array of the same size as the input array
        dp = [0] * len(arr)

        # populate monotonically increasing stack
        for i in range(len(arr)):
            # before pushing an element, make sure all
            # larger and equal elements in the stack are
            # removed
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # calculate the sum of minimums of all subarrays
            # ending at index i
            if stack:
                previousSmaller = stack[-1]
                dp[i] = dp[previousSmaller] + (i - previousSmaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)

        # add all the elements of dp to get the answer
        return sum(dp) % MOD


s = Solution()
tests = [
    ([3, 1, 2, 4],
     17),

    ([11, 81, 94, 43, 3],
        444)
]
for inp, exp in tests:
    res = s.sumSubarrayMins(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
