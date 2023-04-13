"""
Leetcode
946. Validate Stack Sequences (medium)
2023-04-13

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""

from typing import List


class Solution:
    """
    leetcode solution
    Runtime: 76 ms, faster than 42.94% of Python3 online submissions for Validate Stack Sequences.
    Memory Usage: 14 MB, less than 85.31% of Python3 online submissions for Validate Stack Sequences.
    """

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped)


s = Solution()
tests = [
    (([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]),
     True),

    (([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]),
     False),
]
for inp, exp in tests:
    res = s.validateStackSequences(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
