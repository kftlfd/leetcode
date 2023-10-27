"""
Leetcode
5. Longest Palindromic Substring (medium)
2023-10-27

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""


class Solution:
    """
    Memory Limit Exceeded
    """

    def longestPalindrome(self, s: str) -> str:
        memo = {}

        def is_palindrome(i1: int, i2: int) -> bool:
            if i2 - i1 < 1:
                return True

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            ans = s[i1] == s[i2] and is_palindrome(i1 + 1, i2 - 1)

            memo[(i1, i2)] = ans
            return ans

        for length in range(len(s), -1, -1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if is_palindrome(start, end):
                    return s[start:end + 1]


class Solution1:
    """
    leetcode solution 1: Check All Substrings
    Time: O(n^3)
    Space: O(1)
    Runtime: 3736 ms, faster than 22.09% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 16.3 MB, less than 54.45% of Python3 online submissions for Longest Palindromic Substring.
    """

    def longestPalindrome(self, s: str) -> str:

        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Time: O(n^2)
    Space: O(n^2)
    Runtime: 2126 ms, faster than 34.17% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 24.3 MB, less than 9.68% of Python3 online submissions for Longest Palindromic Substring.
    """

    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]


class Solution3:
    """
    leetcode solution 3: Expand From Centers
    Time: O(n^2)
    Space: O(1)
    Runtime: 481 ms, faster than 63.32% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 16.3 MB, less than 54.45% of Python3 online submissions for Longest Palindromic Substring.
    """

    def longestPalindrome(self, s: str) -> str:

        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i:j + 1]


class Solution4:
    """
    leetcode solution 4: Manacher's Algorithm
    https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
    Time: O(n)
    Space: O(n)
    Runtime: 105 ms, faster than 97.33% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 16.4 MB, less than 32.54% of Python3 online submissions for Longest Palindromic Substring.
    """

    def longestPalindrome(self, s: str) -> str:

        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            while (i + 1 + palindrome_radii[i] < n and
                   i - 1 - palindrome_radii[i] >= 0 and
                   s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]

        return longest_palindrome


sol = Solution()
tests = [
    ('babad',
     'bab'),

    ('cbbd',
     'bb'),
]


def check_palindrome(string: str) -> bool:
    if len(string) < 2:
        return True
    return string[0] == string[-1] and check_palindrome(string[1:-1])


for inp, exp in tests:
    res = sol.longestPalindrome(inp)
    if len(res) != len(exp) or (res != exp and not check_palindrome(res)):
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
