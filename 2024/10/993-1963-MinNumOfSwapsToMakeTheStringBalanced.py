"""
Leetcode
2024-10-08
1963. Minimum Number of Swaps to Make the String Balanced
Medium

You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

    It is the empty string, or
    It can be written as AB, where both A and B are balanced strings, or
    It can be written as [C], where C is a balanced string.

You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

 

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.

 

Constraints:

    n == s.length
    2 <= n <= 10^6
    n is even.
    s[i] is either '[' or ']'.
    The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.

Hints:
- Iterate over the string and keep track of the number of opening and closing brackets on each step.
- If the number of closing brackets is ever larger, you need to make a swap.
- Swap it with the opening bracket closest to the end of s.
"""


class Solution:
    """
    Runtime: 185 ms, faster than 78.24% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
    Memory Usage: 27.9 MB, less than 82.95% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
    """

    def minSwaps(self, s: str) -> int:
        swaps = 0

        # q = deque()
        # for c in s:
        #     if not q:
        #         if c == "[":
        #             q.append(c)
        #         elif c == "]":
        #             swaps += 1
        #             q.append("[")
        #     else:
        #         if c == "]":
        #             q.pop()
        #         elif c == "[":
        #             q.append(c)

        stack = 0
        for c in s:
            if stack < 1:
                if c == "]":
                    swaps += 1
                stack += 1
            else:
                stack += 1 if c == "[" else -1

        return swaps


class Solution1:
    """
    leetcode solution
    Runtime: 175 ms, faster than 85.96% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
    Memory Usage: 27.9 MB, less than 45.06% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
    """

    def minSwaps(self, s: str) -> int:
        # stack = deque()
        # unbalanced = 0
        # for ch in s:
        #     # If an opening bracket is encountered, push it in the deque.
        #     if ch == "[":
        #         stack.append(ch)
        #     else:
        #         # If the deque is not empty, pop it.
        #         if stack:
        #             stack.pop()
        #         # Otherwise increase the count of unbalanced brackets.
        #         else:
        #             unbalanced += 1
        # return (unbalanced + 1) // 2

        stack_size = 0
        for ch in s:
            # If character is opening bracket, increment the stack size.
            if ch == "[":
                stack_size += 1
            else:
                # If the character is closing bracket, and we have an opening bracket, decrease
                # the stack size.
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2


class Solution2:
    """
    https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/solution/2663976
    Runtime: 321 ms, faster than 38.19% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
    Memory Usage: 27.9 MB, less than 45.06% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
    """

    def minSwaps(self, s: str) -> int:
        balance = count = 0
        for c in s:
            balance += c == '['
            balance -= c == ']'
            if balance < 0:
                balance = 1
                count += 1
        return count
