"""
Leetcode
2025-07-23
1717. Maximum Score From Removing Substrings
Medium

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

    Remove substring "ab" and gain x points.
        For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    Remove substring "ba" and gain y points.
        For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

 

Constraints:

    1 <= s.length <= 105
    1 <= x, y <= 104
    s consists of lowercase English letters.


Hint 1
Note that it is always more optimal to take one type of substring before another
Hint 2
You can use a stack to handle erasures
"""


class Solution:
    """
    Runtime 2081ms Beats 5.16%
    Memory 18.94MB Beats 90.97%
    """

    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0

        stack = []

        priority = [["a", "b"], ["b", "a"]]
        scores = [x, y]
        if y > x:
            priority = [["b", "a"], ["a", "b"]]
            scores = [y, x]

        for idx, c in enumerate(s):
            if c in ("a", "b"):
                stack.append(c)
                if idx != len(s) - 1:
                    continue

            if not stack:
                continue

            for turn in (0, 1):
                changes = True
                while changes:
                    changes = False
                    i = 1
                    while i <= len(stack):
                        if stack[i-1:i+1] == priority[turn]:
                            i -= 2
                            stack.pop(i+1)
                            stack.pop(i+1)
                            ans += scores[turn]
                            changes = True
                        i += 1

            stack = []

        return ans


class Solution1:
    """
    leetcode solution 1: Greedy Way (Stack)
    Runtime 199ms Beats 64.52%
    Memory 19.12MB Beats 83.23%
    """

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        high_priority_pair = "ab" if x > y else "ba"
        low_priority_pair = "ba" if high_priority_pair == "ab" else "ab"

        # First pass: remove high priority pair
        string_after_first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(string_after_first_pass)) // 2

        # Calculate score from first pass
        total_score += removed_pairs_count * max(x, y)

        # Second pass: remove low priority pair
        string_after_second_pass = self.remove_substring(
            string_after_first_pass, low_priority_pair
        )
        removed_pairs_count = (
            len(string_after_first_pass) - len(string_after_second_pass)
        ) // 2

        # Calculate score from second pass
        total_score += removed_pairs_count * min(x, y)

        return total_score

    def remove_substring(self, input: str, target_pair: str) -> str:
        char_stack = []

        # Iterate through each character in the input string
        for current_char in input:
            # Check if current character forms the target pair with the top of the stack
            if (
                current_char == target_pair[1]
                and char_stack
                and char_stack[-1] == target_pair[0]
            ):
                char_stack.pop()  # Remove the matching character from the stack
            else:
                char_stack.append(current_char)

        # Reconstruct the remaining string after removing target pairs
        return "".join(char_stack)


class Solution2:
    """
    leetcode solution 2: Greedy Way (Without Stack)
    Runtime 313ms Beats 24.51%
    Memory 19.28MB Beats 76.13%
    """

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        s = list(s)

        if x > y:
            # Remove "ab" first (higher points), then "ba"
            total_points += self.remove_substring(s, "ab", x)
            total_points += self.remove_substring(s, "ba", y)
        else:
            # Remove "ba" first (higher or equal points), then "ab"
            total_points += self.remove_substring(s, "ba", y)
            total_points += self.remove_substring(s, "ab", x)

        return total_points

    def remove_substring(
        self, input_string, target_substring, points_per_removal
    ):
        total_points = 0
        write_index = 0

        # Iterate through the string
        for read_index in range(0, len(input_string)):
            # Add the current character
            input_string[write_index] = input_string[read_index]
            write_index += 1

            # Check if we've written at least two characters and
            # they match the target substring
            if (
                write_index > 1
                and input_string[write_index - 2] == target_substring[0]
                and input_string[write_index - 1] == target_substring[1]
            ):
                write_index -= 2
                total_points += points_per_removal

        # Trim the list to remove any leftover characters
        del input_string[write_index:]

        return total_points


class Solution3:
    """
    leetcode solution 3: Greedy Way (Counting)
    Runtime 171ms Beats 91.61%
    Memory 18.05MB Beats 96.13%
    """

    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Ensure "ab" always has higher points than "ba"
        if x < y:
            # Reverse the string to maintain logic
            s = s[::-1]
            # Swap points
            x, y = y, x

        a_count, b_count, total_points = 0, 0, 0

        for i in range(len(s)):
            if s[i] == "a":
                a_count += 1
            elif s[i] == "b":
                if a_count > 0:
                    # Can form "ab", remove it and add points
                    a_count -= 1
                    total_points += x
                else:
                    # Can't form "ab", keep 'b' for potential future "ba"
                    b_count += 1
            else:
                # Non 'a' or 'b' character encountered
                # Calculate points for any remaining "ba" pairs
                total_points += min(b_count, a_count) * y
                # Reset counters for next segment
                a_count = b_count = 0

        # Calculate points for any remaining "ba" pairs at the end
        total_points += min(b_count, a_count) * y

        return total_points
