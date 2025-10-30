"""
Leetcode
2025-10-30
1526. Minimum Number of Increments on Subarrays to Form a Target Array
Hard

You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

In one operation you can choose any subarray from initial and increment each value by one.

Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.

Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]

Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].

 

Constraints:

    1 <= target.length <= 10^5
    1 <= target[i] <= 10^5


Hint 1
For a given range of values in target, an optimal strategy is to increment the entire range by the minimum value. The minimum in a range could be obtained with Range minimum query or Segment trees algorithm.
"""

from collections import deque
from typing import List


class Solution01:
    """
    Runtime 101ms Beats 10.16%
    Memory 26.71MB Beats 36.79%
    """

    def minNumberOperations(self, target: List[int]) -> int:
        st = deque()
        ans = 0

        for num in target:
            popped = 0
            while st and st[-1] > num:
                popped = st.pop()
            prev = st[-1] if st else 0
            if num > prev:
                ans += 0 if popped > 0 else num - prev
                st.append(num)

        return ans


class Solution02:
    """
    with editorial hint
    Runtime 93ms Beats 12.19%
    Memory 26.68MB Beats 76.07%
    """

    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(max(target[i] - target[i - 1], 0) for i in range(1, len(target)))


class Solution1:
    """
    leetcode solution
    Runtime 91ms Beats 14.00%
    Memory 26.66MB Beats 76.07%
    """

    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans
