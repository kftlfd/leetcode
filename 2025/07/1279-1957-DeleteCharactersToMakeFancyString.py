"""
Leetcode
2025-07-21
1957. Delete Characters to Make Fancy String
Easy

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

 

Constraints:

    1 <= s.length <= 10^5
    s consists only of lowercase English letters.


"""


class Solution:
    """
    Runtime 267ms Beats 87.28%
    Memory 19.90MB Beats 25.65%
    """

    def makeFancyString(self, s: str) -> str:
        ans = list(s[:2])

        for i in range(2, len(s)):
            c = s[i]
            if c != ans[-1] or c != ans[-2]:
                ans.append(c)

        return "".join(ans)


class Solution2:
    """
    leetcode solution 2: In-Place Two-Pointer Approach
    Runtime 323ms Beats 62.63%
    Memory 19.92MB Beats19.48%
    """

    def makeFancyString(self, s: str) -> str:
        # If size of string is less than 3, return it.
        if len(s) < 3:
            return s

        # Convert the string to a list for mutability.
        s_list = list(s)
        j = 2

        # Iterate through the string from index 2.
        for i in range(2, len(s)):
            # If the current character is not equal to the previously inserted
            # two characters, then we can add it to the result.
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        # Resize the list to the number of valid characters and join it back into a string.
        return "".join(s_list[:j])
