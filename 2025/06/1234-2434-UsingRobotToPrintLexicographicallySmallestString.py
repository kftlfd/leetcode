"""
Leetcode
2025-06-06
2434. Using a Robot to Print the Lexicographically Smallest String
Medium

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

    Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
    Remove the last character of a string t and give it to the robot. The robot will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".

Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".

 

Constraints:

    1 <= s.length <= 10^5
    s consists of only English lowercase letters.


Hint 1
If there are some character “a” ’ s in the string, they can be written on paper before anything else.
Hint 2
Every character in the string before the last “a” should be written in reversed order.
Hint 3
After the robot writes every “a” on paper, the same holds for other characters “b”, ”c”, …etc.
"""


from collections import Counter


class Solution:
    """
    Wrong Answer
    """

    def robotWithString(self, s: str) -> str:
        ans = []
        n = len(s)
        i = 0
        while i < n:
            for c in range(26):
                cur = chr(c + 97)
                j = i
                while j < n and s[j] != cur:
                    j += 1
                if j < n:
                    ans.append(s[i:j+1][::-1])
                    i = j + 1
                    break
        return "".join(ans)


class Solution1:
    """
    leetcode solution: Greedy + Stack
    Runtime 491ms Beats 52.67%
    Memory 20.30MB Beats 95.04%
    """

    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        res = []
        minCharacter = "a"
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while minCharacter != "z" and cnt[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            while stack and stack[-1] <= minCharacter:
                res.append(stack.pop())
        return "".join(res)
