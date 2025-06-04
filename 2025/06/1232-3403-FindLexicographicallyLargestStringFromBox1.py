"""
Leetcode
2025-06-04
3403. Find the Lexicographically Largest String From the Box I
Medium

You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

    word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
    All the split words are put into a box.

Find the

string from the box after all the rounds are finished.

 

Example 1:

Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

    "d" and "bca".
    "db" and "ca".
    "dbc" and "a".

Example 2:

Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".

 

Constraints:

    1 <= word.length <= 5 * 10^3
    word consists only of lowercase English letters.
    1 <= numFriends <= word.length

Hint 1
Find lexicographically largest substring of size n - numFriends + 1 or less starting at every index.
"""


class Solution00:
    """
    Runtime 4974ms Beats 5.30%
    Memory 18.68MB Beats 11.36%
    """

    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if numFriends == 1:
            return word

        def is_lex_larger(a: int, b: int) -> bool:
            if a >= n or b >= n:
                if a >= n and b >= n:
                    return False
                return b < n

            if word[a] == word[b]:
                return is_lex_larger(a + 1, b + 1)

            return word[b] > word[a]

        ans_start = 0
        for i in range(1, n):
            if is_lex_larger(ans_start, i):
                ans_start = i

        ans_len = n - numFriends + 1
        ans = word[ans_start:ans_start + ans_len]

        return ans


class Solution01:
    """
    Runtime 19ms Beats 37.12%
    Memory 17.94MB Beats 49.24%
    """

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        ans_len = n - numFriends + 1

        def is_lex_larger(a: int, b: int) -> bool:
            str_a = word[a:a + ans_len]
            str_b = word[b:b + ans_len]
            return str_b > str_a

        ans_start = 0
        for i in range(1, n):
            if is_lex_larger(ans_start, i):
                ans_start = i

        ans = word[ans_start:ans_start + ans_len]

        return ans


class Solution1:
    """
    leetcode solution 1: Enumeration
    Runtime 23ms Beats 29.55%
    Memory 17.81MB Beats 64.39%
    """

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        for i in range(n):
            res = max(res, word[i: min(i + n - numFriends + 1, n)])
        return res


class Solution2:
    """
    leetcode solution 2: Two Pointers
    Runtime 8ms Beats 85.61%
    Memory 17.96MB Beats 49.24%
    """

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        last = self.lastSubstring(word)
        n, m = len(word), len(last)
        return last[: min(m, n - numFriends + 1)]

    def lastSubstring(self, s: str) -> str:
        i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        return s[i:]
