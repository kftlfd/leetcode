"""
Leetcode
2026-09-26
1807. Evaluate the Bracket Pairs of a String
Medium

You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

    For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".

You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:

    Replace keyi and the bracket pair with the key's corresponding valuei.
    If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).

Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.

 

Example 1:

Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

Example 2:

Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

Example 3:

Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

 

Constraints:

    1 <= s.length <= 10^5
    0 <= knowledge.length <= 10^5
    knowledge[i].length == 2
    1 <= keyi.length, valuei.length <= 10
    s consists of lowercase English letters and round brackets '(' and ')'.
    Every open bracket '(' in s will have a corresponding close bracket ')'.
    The key in each bracket pair of s will be non-empty.
    There will not be any nested bracket pairs in s.
    keyi and valuei consist of lowercase English letters.
    Each keyi in knowledge is unique.

    
Hint 1
Process pairs from right to left to handle repeats
Hint 2
Keep track of the current enclosed string using another string
"""


class Solution:
    """
    Runtime 34ms Beats 95.02%
    Memory 51.89MB Beats 28.97%
    """

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hm: dict[str, str] = {}
        for key, val in knowledge:
            hm[key] = val

        ans: list[str] = []

        is_key = False
        key = ""

        for c in s:
            if c == "(":
                is_key = True
                key = ""
            elif c == ")":
                ans.append(hm.get(key, "?"))
                is_key = False
            else:
                if is_key:
                    key += c
                else:
                    ans.append(c)

        return "".join(ans)


class Solution1:
    """
    leetcode solution
    Runtime 51ms Beats 57.94%
    Memory 52.00MB Beats 21.81%
    """

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans, start = [], -1
        for i, c in enumerate(s):
            if c == "(":
                start = i
            elif c == ")":
                ans.append(d.get(s[start + 1: i], "?"))
                start = -1
            elif start < 0:
                ans.append(c)
        return "".join(ans)
