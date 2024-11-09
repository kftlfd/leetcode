"""
Leetcode
2024-11-09
3133. Minimum Array End
Medium

You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

 

Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

 

Constraints:

    1 <= n, x <= 10^8

Hints:
- Each element of the array should be obtained by “merging” x and v where v = 0, 1, 2, …(n - 1).
- To merge x with another number v, keep the set bits of x untouched, for all the other bits, fill the set bits of v from right to left in order one by one.
- So the final answer is the “merge” of x and n - 1.
"""


class Solution:
    """
    wrong answer
    """

    def minEnd(self, n: int, x: int) -> int:
        return self.merge(x, n - 1)

    def merge(self, x: int, v: int) -> int:
        ans = x
        cur_bit = 1
        ins_bit = 1
        while cur_bit <= v:
            if v & cur_bit == cur_bit:
                while ans & ins_bit == ins_bit:
                    ins_bit <<= 1
                ans |= ins_bit
            ins_bit <<= 1
            cur_bit <<= 1
        return ans


class Solution1:
    """
    leetcode solution 1: Consecutive ORing
    """

    def minEnd(self, n: int, x: int) -> int:
        result = x

        # Step 1: Iterate n-1 times (since we already initialized result with x)
        while n > 1:
            # Step 2: Increment result and perform bitwise OR with x
            result = (result + 1) | x
            n -= 1

        return result


class Solution2:
    """
    leetcode solution 2: Bit Manipulation and Binary Construction
    """

    def minEnd(self, n: int, x: int) -> int:
        result = 0
        # Reducing n by 1 to exclude x from the iteration
        n -= 1

        # Step 1: Initialize lists to hold the binary representation of x and n-1
        binaryX = [0] * 64  # Binary representation of x
        binaryN = [0] * 64  # Binary representation of n-1

        # Step 2: Build binary representations of x and n-1
        for i in range(64):
            bit = (x >> i) & 1  # Extract i-th bit of x
            binaryX[i] = bit

            bit = (n >> i) & 1  # Extract i-th bit of n-1
            binaryN[i] = bit

        posX = 0
        posN = 0

        # Step 3: Combine binary representation of x and n-1
        while posX < 63:
            # Traverse binaryX until we find a 0 bit
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            # Copy bits from binaryN (n-1) into binaryX (x) starting from the first 0
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        # Step 4: Rebuild the final result from the combined binary representation
        for i in range(64):
            if binaryX[i] == 1:
                # convert binary bit to decimal value
                result += pow(2, i)

        return result


class Solution3:
    """
    leetcode solution 3: Bitmasking with Logical Operations
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Minimum Array End.
    Memory Usage: 16.7 MB, less than 33.33% of Python3 online submissions for Minimum Array End.
    """

    def minEnd(self, n: int, x: int) -> int:
        result = x
        n -= 1  # Reducing n by 1 to exclude x from the iteration
        mask = 1

        # Step 1: Iterate while n > 0, using mask for bit positions
        while n > 0:
            # Step 2: If the corresponding bit in x is 0
            if (mask & x) == 0:
                # Set the bit in result based on least significant bit of n
                result |= (n & 1) * mask
                # Shift n right by 1 to process next bit
                n >>= 1
            # Shift mask left by 1 for next iteration
            mask <<= 1

        return result


s = Solution()
tests = [
    ((100000000, 99999999),
     52428799999999),
]
for inp, exp in tests:
    res = s.minEnd(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
