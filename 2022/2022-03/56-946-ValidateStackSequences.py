'''
Leetcode
946. Validate Stack Sequences (medium)
2022-03-16

Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push 
and pop operations on an initially empty stack, or false otherwise.

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
'''

from typing import List



# try 1
# Runtime: 121 ms, faster than 31.67% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.2 MB, less than 63.80% of Python3 online submissions for Validate Stack Sequences.
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        st = []

        while pushed or popped:

            if st and popped and popped[0] == st[-1]:
                st.pop()
                popped.pop(0)

            elif not pushed:
                return False
            
            elif pushed: st.append(pushed.pop(0))

        return not st



# leetcode solution
# https://leetcode.com/problems/validate-stack-sequences/solution/
# Runtime: 108 ms, faster than 45.48% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.1 MB, less than 93.97% of Python3 online submissions for Validate Stack Sequences.
class Solution1:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)



s = Solution1()
tests = [
    ([1,2,3,4,5], [4,5,3,2,1]),
    ([1,2,3,4,5], [4,3,5,1,2])
]
for pushed, popped in tests:
    print(pushed, popped)
    print(s.validateStackSequences(pushed, popped))
