"""
Leetcode
650. 2 Keys Keyboard
Medium
2024-08-19

There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:

Input: n = 1
Output: 0

 

Constraints:

    1 <= n <= 1000

Hints:
- How many characters may be there in the clipboard at the last step if n = 3? n = 7? n = 10? n = 24?    
"""


class Solution1:
    """
    leetcode solution 1: Recursion / Backtracking
    Runtime: 592 ms, faster than 10.59% of Python3 online submissions for 2 Keys Keyboard.
    Memory Usage: 16.5 MB, less than 61.96% of Python3 online submissions for 2 Keys Keyboard.
    """

    def __init__(self):
        self.n = 0

    def _min_steps_helper(self, curr_len, paste_len):
        # base case: reached n A's, don't need more operations
        if curr_len == self.n:
            return 0
        # base case: exceeded n `A`s, not a valid sequence, so
        # return max value
        if curr_len > self.n:
            return 1000

        # copy all + paste
        opt1 = 2 + self._min_steps_helper(curr_len * 2, curr_len)
        # paste
        opt2 = 1 + self._min_steps_helper(curr_len + paste_len, paste_len)

        return min(opt1, opt2)

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n
        # first step is always a Copy All operation
        return 1 + self._min_steps_helper(1, 1)


class Solution2:
    """
    leetcode solution 2: Top-Down Dynamic Programming
    Runtime: 151 ms, faster than 45.56% of Python3 online submissions for 2 Keys Keyboard.
    Memory Usage: 20.8 MB, less than 23.92% of Python3 online submissions for 2 Keys Keyboard.
    """

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n

        self.memo = [[0] * (n // 2 + 1) for _ in range(n + 1)]
        return 1 + self._min_steps_helper(1, 1)

    def _min_steps_helper(self, curr_len: int, paste_len: int) -> int:
        if curr_len == self.n:
            return 0
        if curr_len > self.n:
            return 1000

        # return result if it has been calculated already
        if self.memo[curr_len][paste_len] != 0:
            return self.memo[curr_len][paste_len]

        opt1 = 1 + self._min_steps_helper(curr_len + paste_len, paste_len)
        opt2 = 2 + self._min_steps_helper(curr_len * 2, curr_len)
        self.memo[curr_len][paste_len] = min(opt1, opt2)
        return self.memo[curr_len][paste_len]


class Solution3:
    """
    leetcode solution 3: Bottom-Up Dynamic Programming
    Runtime: 219 ms, faster than 32.91% of Python3 online submissions for 2 Keys Keyboard.
    Memory Usage: 16.4 MB, less than 88.15% of Python3 online submissions for 2 Keys Keyboard.
    """

    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)

        # Base case
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                # Copy All and Paste (i-j) / j times
                # for all valid j's
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]


class Solution4:
    """
    leetcode solution 4: Prime Factorization
    Runtime: 40 ms, faster than 75.74% of Python3 online submissions for 2 Keys Keyboard.
    Memory Usage: 16.5 MB, less than 88.15% of Python3 online submissions for 2 Keys Keyboard.
    """

    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
