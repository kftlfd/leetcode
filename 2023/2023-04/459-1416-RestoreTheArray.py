"""
Leetcode
1416. Restore The Array (hard)
2023-04-23

A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]

Example 2:
Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.

Example 3:
Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
"""


class Solution1:
    """
    leetcode solution 1: Dynamic Programming (Top Down)
    Runtime: 1627 ms, faster than 58.90% of Python3 online submissions for Restore The Array.
    Memory Usage: 121.5 MB, less than 46.58% of Python3 online submissions for Restore The Array.
    """

    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)
        mod = 10**9 + 7
        dp = [0] * (m + 1)

        # Number of possible splits for s[start ~ m-1]
        def dfs(start: int) -> int:
            # if we have already updated dp[start], return it
            if dp[start] != 0:
                return dp[start]

            # if empty string, there is only 1 split
            if start == m:
                return 1

            # number can't have leading zeroes
            if s[start] == '0':
                return 0

            # for all possible starting number, add the number of arrays
            # that can be printed as the remaining string to count
            count = 0
            for end in range(start, m):
                curr_number = s[start:end+1]
                if int(curr_number) > k:
                    break
                count += dfs(end + 1)

            # update dp[start]
            dp[start] = count % mod
            return count

        return dfs(0) % mod


class Solution2:
    """
    leetcode solution 2: Dynamic Programming (Bottom Up)
    Runtime: 1619 ms, faster than 58.90% of Python3 online submissions for Restore The Array.
    Memory Usage: 18.4 MB, less than 57.53% of Python3 online submissions for Restore The Array.
    """

    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)
        mod = 10**9 + 7

        # dp[i] records the number of arrays that can be printed as
        # the prefix substring s[0 ~ i-1]
        dp = [1] + [0] * m

        # iterate over every digit
        for start in range(m):
            if s[start] == '0':
                continue

            # iterate over ending digit end and find all valid numbers
            # s[start ~ end]
            for end in range(start, m):
                curr_number = s[start:end+1]
                if int(curr_number) > k:
                    break

                # if s[start ~ end] is valid, increment dp[end+1] by dp[start]
                dp[end+1] += dp[start]
                dp[end+1] %= mod

        return dp[-1]


class Solution3:
    """
    leetcode solution 3: Dynamic Programming (memmory optimized)
    Runtime: 1928 ms, faster than 35.61% of Python3 online submissions for Restore The Array.
    Memory Usage: 15.7 MB, less than 95.89% of Python3 online submissions for Restore The Array.
    """

    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)
        n = len(str(k))
        mod = 10**9 + 7

        # dp[i % (n+1)] records the number of arrays that can be printed as
        # the prefix substring s[0 ~ i-1]
        dp = [1] + [0] * m

        # iterate over every digit, for each digit s[start]
        for start in range(m):
            if s[start] == '0':
                dp[start % (n+1)] = 0
                continue

            # iterate over ending digit end and find all valid numbers
            # s[start ~ end]
            for end in range(start, m):
                if int(s[start:end+1]) > k:
                    break

                # if s[start ~ end] is valid, increment dp[(end+1) % (n+1)] by dp[start]
                dp[(end+1) % (n+1)] += dp[start % (n+1)]
                dp[(end+1) % (n+1)] %= mod

            dp[start % (n+1)] = 0

        return dp[m % (n+1)]


sol = Solution3()
tests = [
    (("1000", 10000),
     1),

    (("1000", 10),
     0),

    (("1317", 2000),
     8),
]
for inp, exp in tests:
    res = sol.numberOfArrays(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
