"""
Leetcode
2025-09-16
2197. Replace Non-Coprime Numbers in Array
Hard

You are given an array of integers nums. Perform the following steps:

    Find any two adjacent numbers in nums that are non-coprime.
    If no such numbers are found, stop the process.
    Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
    Repeat this process as long as you keep finding two adjacent non-coprime numbers.

Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

 

Example 1:

Input: nums = [6,4,3,2,7,6,2]
Output: [12,7,6]
Explanation: 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [12,7,6].
Note that there are other ways to obtain the same resultant array.

Example 2:

Input: nums = [2,2,1,1,3,3,3]
Output: [2,1,1,3]
Explanation: 
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
- (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [2,1,1,3].
Note that there are other ways to obtain the same resultant array.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    The test cases are generated such that the values in the final array are less than or equal to 108.


Hint 1
Notice that the order of merging two numbers into their LCM does not matter so we can greedily merge elements to its left if possible.
Hint 2
If a new value is formed, we should recursively check if it can be merged with the value to its left.
Hint 3
To simulate the merge efficiently, we can maintain a stack that stores processed elements. When we iterate through the array, we only compare with the top of the stack (which is the value to its left).
"""

import math
from typing import List


class Solution:
    """
    Runtime 163ms Beats 35.87%
    Memory 31.90MB Beats 21.74%
    """

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)

            while len(stack) >= 2 and math.gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(math.lcm(a, b))

        return stack


class Solution1:
    """
    sample 99ms solution
    Runtime 107ms Beats 94.56%
    Memory 30.54MB Beats 96.74%
    """

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        a = [1]
        for i in nums:
            while (d := math.gcd(a[-1], i)) != 1:
                i = a.pop() * i//d
            a.append(i)
        return a[1:]
