"""
Leetcode
2026-03-14
1415. The k-th Lexicographical String of All Happy Strings of Length n
Medium

A happy string is a string that:

    consists only of letters of the set ['a', 'b', 'c'].
    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

 

Constraints:

    1 <= n <= 10
    1 <= k <= 100


"""


class Solution:
    """
    Runtime 43ms Beats 37.86%
    Memory 29.70MB Beats 21.60%
    """

    def getHappyString(self, n: int, k: int) -> str:
        strings = []

        def gen_strs(cur: str):
            if len(cur) >= n:
                strings.append(cur)
                return
            if cur[-1] != "a":
                gen_strs(cur + "a")
            if cur[-1] != "b":
                gen_strs(cur + "b")
            if cur[-1] != "c":
                gen_strs(cur + "c")
        gen_strs("a")
        gen_strs("b")
        gen_strs("c")

        if k > len(strings):
            return ""

        return strings[k - 1]


class Solution1:
    """
    leetcode solution 1: Backtracking (Optimized)
    Runtime 49ms Beats 29.29%
    Memory 19.48MB Beats 78.17%
    """

    def getHappyString(self, n: int, k: int) -> str:
        current_string = ""
        happy_strings = []
        # Generate all happy strings of length n
        self.generate_happy_strings(n, current_string, happy_strings)

        # Check if there are at least k happy strings
        if len(happy_strings) < k:
            return ""

        return happy_strings[k - 1]

    def generate_happy_strings(
        self, n: int, current_string: str, happy_strings: list
    ):
        # If the current string has reached the desired length, add it to the list
        if len(current_string) == n:
            happy_strings.append(current_string)
            return

        # Try adding each character ('a', 'b', 'c') to the current string
        for current_char in ["a", "b", "c"]:
            # Skip if the current character is the same as the last character
            if len(current_string) > 0 and current_string[-1] == current_char:
                continue

            # Recursively generate the next character
            self.generate_happy_strings(
                n, current_string + current_char, happy_strings
            )


class Solution2:
    """
    leetcode solution 2: Optimized Recursion
    Runtime 7ms Beats 62.14%
    Memory 19.39MB Beats 92.65%
    """

    def getHappyString(self, n: int, k: int) -> str:
        self.current_string = ""
        self.result = ""
        self.index_in_sorted_list = 0

        # Generate happy strings and track the k-th string
        self.generate_happy_strings(n, k)
        return self.result

    def generate_happy_strings(self, n, k):
        # If the current string has reached the desired length
        if len(self.current_string) == n:
            # Increment the count of generated strings
            self.index_in_sorted_list += 1

            # If this is the k-th string, store it in the result
            if self.index_in_sorted_list == k:
                self.result = self.current_string
            return

        # Try adding each character ('a', 'b', 'c') to the current string
        for current_char in ["a", "b", "c"]:
            # Skip if the current character is the same as the last one
            if (
                len(self.current_string) > 0
                and self.current_string[-1] == current_char
            ):
                continue

            self.current_string += current_char

            # Recursively generate the next character
            self.generate_happy_strings(n, k)

            # If the result is found, stop further processing
            if self.result != "":
                return

            # Backtrack by removing the last character
            self.current_string = self.current_string[:-1]


class Solution3:
    """
    leetcode solution 3: Iterative Using a Stack
    Runtime 3ms Beats 82.52%
    Memory 19.22MB Beats 97.88%
    """

    def getHappyString(self, n: int, k: int) -> str:
        strings_stack = []
        index_in_sorted_list = 0
        strings_stack.append("")  # Start with an empty string

        while strings_stack:
            current_string = strings_stack.pop()

            # If we have built a string of length n, count it
            if len(current_string) == n:
                index_in_sorted_list += 1
                # If we reach the k-th happy string, return it
                if index_in_sorted_list == k:
                    return current_string
                continue

            # Expand the current string by adding 'a', 'b', or 'c'
            # Ensuring lexicographic order by pushing in reverse
            for current_char in reversed(["a", "b", "c"]):
                # Avoid consecutive identical characters
                if (
                    len(current_string) == 0
                    or current_string[-1] != current_char
                ):
                    strings_stack.append(current_string + current_char)
        return ""


class Solution4:
    """
    leetcode solution 4: Combinatorics
    Runtime 4ms Beats 71.71%
    Memory 19.35MB Beats 92.65%
    """

    def getHappyString(self, n: int, k: int) -> str:
        # Calculate the total number of happy strings of length n
        total = 3 * (1 << (n - 1))

        # If k is greater than the total number of happy strings, return an empty string
        if k > total:
            return ""

        result = ["a"] * n  # Initialize result with 'a' characters

        # Define mappings for the next smallest and greatest valid characters
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        # Calculate the starting indices for strings beginning with 'a', 'b', and 'c'
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        # Determine the first character based on the value of k
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        # Iterate through the remaining positions in the result string
        for char_index in range(1, n):
            # Calculate the midpoint of the group for the current character position
            midpoint = 1 << (n - char_index - 1)

            # Determine the next character based on the value of k
            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)
