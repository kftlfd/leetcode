"""
Leetcode
1404. Number of Steps to Reduce a Number in Binary Representation to One
Medium
2024-05-29

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

    If the current number is even, you have to divide it by 2.

    If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:

Input: s = "1"
Output: 0

 

Constraints:

    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'

Hints:
- Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.
- Simulate the steps described in the binary string.    
"""


from functools import cache


class Solution:
    """
    Runtime: 36 ms, faster than 60.15% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
    Memory Usage: 16.4 MB, less than 94.14% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
    """

    def numSteps(self, s: str) -> int:
        steps = 0
        carry = False

        for i in range(len(s)-1, 0, -1):
            c = s[i] == '1'
            if carry:
                carry = c
                c = not c

            steps += 1 + c
            carry |= c

        # i = 0
        steps += carry

        return steps


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime: 39 ms, faster than 40.00% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
    Memory Usage: 16.5 MB, less than 94.14% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
    """

    def numSteps(self, s: str) -> int:
        N = len(s)

        operations = 0
        carry = 0
        for i in range(N - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1

        return operations + carry


class Solution3:
    """
    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/solution/2424855
    Runtime: 35 ms, faster than 67.52% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
    Memory Usage: 17.3 MB, less than 6.77% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
    """

    def numSteps(self, s: str) -> int:
        n = int(s, 2)

        @cache
        def dp(n):
            if n == 1:
                return 0
            if n == 2:
                return 1
            if n % 2 == 0:
                return dp(n//2) + 1
            return dp(n//2+1) + 2

        return dp(n)
