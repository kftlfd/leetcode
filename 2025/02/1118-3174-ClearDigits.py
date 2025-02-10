"""
Leetcode
2025-02-10
3174. Clear Digits
Easy

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".

 

Constraints:

    1 <= s.length <= 100
    s consists only of lowercase English letters and digits.
    The input is generated such that it is possible to delete all digits.


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.72MB Beats 43.55%
    """

    def clearDigits(self, s: str) -> str:
        ans = []

        for c in s:
            if not c.isdigit():
                ans.append(c)
            elif ans:
                ans.pop()

        return "".join(ans)


class Solution3:
    """
    leetcode solution 3: In-place
    Runtime 0ms Beats 100.00%
    Memory 17.71MB Beats 43.55%
    """

    def clearDigits(self, s: str) -> str:
        # This variable keeps track of the actual length of the resulting string
        answer_length = 0
        s = list(s)

        # Iterate through each character in the input string
        for char_index in range(len(s)):

            # If the current character is a digit
            if s[char_index].isdigit():
                # Decrement answerLength to remove the last character from the result
                answer_length = max(answer_length - 1, 0)
            else:
                # Place the character in the "answer" portion of the string
                s[answer_length] = s[char_index]
                answer_length += 1

        # Resize the string to match the actual length of the answer
        s = s[:answer_length]

        return "".join(s)
