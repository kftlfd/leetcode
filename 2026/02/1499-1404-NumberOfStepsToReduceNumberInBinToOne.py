"""
Leetcode
2026-02-26
1404. Number of Steps to Reduce a Number in Binary Representation to One
Medium

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
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:

Input: s = "1"
Output: 0

 

Constraints:

    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'


Hint 1
Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.
Hint 2
Simulate the steps described in the binary string.
"""


from typing import List


class Solution:
    """
    Runtime 1ms Beats 49.88%
    Memory 19.36MB Beats 54.01%
    """

    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        steps = 0

        while num > 1:
            if num & 1 == 1:
                num += 1
            else:
                num >>= 1
            steps += 1

        return steps


class Solution1:
    """
    leetcode solution 1: Simulation
    Runtime 3ms Beats 40.39%
    Memory 19.39MB Beats 54.01%
    """

    def numSteps(self, s: str) -> int:
        sl = list(s)
        operations = 0

        while len(sl) > 1:
            N = len(sl)

            if sl[N - 1] == "0":
                self.divide_by_two(sl)
            else:
                self.add_one(sl)

            operations += 1

        return operations

    def divide_by_two(self, s: List[str]):
        s.pop()

    def add_one(self, s: List[str]):
        i = len(s) - 1

        # Iterating while the character is 1 and changing to 0
        while i >= 0 and s[i] != "0":
            s[i] = "0"
            i -= 1

        if i < 0:
            s.insert(0, "1")
        else:
            s[i] = "1"


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime 0ms Beats 100.00%
    Memory 19.28MB Beats 80.78%
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
