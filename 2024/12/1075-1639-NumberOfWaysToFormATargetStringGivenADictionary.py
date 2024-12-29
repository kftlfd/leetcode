"""
Leetcode
2024-12-29
1639. Number of Ways to Form a Target String Given a Dictionary
Solved
Hard

You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

    target should be formed from left to right.
    To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
    Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
    Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 1000
    All strings in words have the same length.
    1 <= target.length <= 1000
    words[i] and target contain only lowercase English letters.

Hint 1
For each index i, store the frequency of each character in the ith row.
Hint 2
Use dynamic programing to calculate the number of ways to get the target string using the frequency array.
"""

from typing import List, Optional


class Solution1:
    """
    leetcode solution 1: Top-down Dynamic Programming
    """

    def numWays(self, words: List[str], target: str) -> int:
        dp = [[-1] * len(target) for _ in range(len(words[0]))]
        char_frequency = [[0] * 26 for _ in range(len(words[0]))]

        # Store the frequency of every character at every index.
        for i in range(len(words)):
            for j in range(len(words[0])):
                character = ord(words[i][j]) - 97
                char_frequency[j][character] += 1
        return self.__get_words(words, target, 0, 0, dp, char_frequency)

    def __get_words(
        self, words, target, words_index, target_index, dp, char_frequency
    ):
        if target_index == len(target):
            return 1
        if (
            words_index == len(words[0])
            or len(words[0]) - words_index < len(target) - target_index
        ):
            return 0

        if dp[words_index][target_index] != -1:
            return dp[words_index][target_index]

        count_ways = 0
        cur_pos = ord(target[target_index]) - 97
        # Don't match any character of target with any word.
        count_ways += self.__get_words(
            words, target, words_index + 1, target_index, dp, char_frequency
        )
        # Multiply the number of choices with getWords and add it to count.
        count_ways += char_frequency[words_index][cur_pos] * self.__get_words(
            words, target, words_index + 1, target_index + 1, dp, char_frequency
        )

        dp[words_index][target_index] = count_ways % 1000000007
        return dp[words_index][target_index]


class Solution2:
    """
    leetcode solution 2: Bottom-up Dynamic Programming
    """

    def numWays(self, words: List[str], target: str) -> int:
        word_length = len(words[0])
        target_length = len(target)
        mod = 1000000007

        # Step 1: Calculate frequency of each character at every index in
        # "words".
        char_frequency = [[0] * 26 for _ in range(word_length)]
        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1

        # Step 2: Initialize a DP table.
        dp = [[0] * (target_length + 1) for _ in range(word_length + 1)]

        # Base case: There is one way to form an empty target string.
        for curr_word in range(word_length + 1):
            dp[curr_word][0] = 1

        # Step 3: Fill the DP table.
        for curr_word in range(1, word_length + 1):
            for curr_target in range(1, target_length + 1):
                # Carry over the previous value (not using this index of
                # "words").
                dp[curr_word][curr_target] = dp[curr_word - 1][curr_target]

                # Add ways using the current index of "words" if the characters
                # match.
                cur_pos = ord(target[curr_target - 1]) - ord("a")
                dp[curr_word][curr_target] += (
                    char_frequency[curr_word - 1][cur_pos]
                    * dp[curr_word - 1][curr_target - 1]
                ) % mod
                dp[curr_word][curr_target] %= mod

        # Step 4: The result is in dp[word_length][target_length].
        return dp[word_length][target_length]


class Solution3:
    """
    leetcode solution 3: Optimized Bottom-up Dynamic Programmning
    """

    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        word_length = len(words[0])
        target_length = len(target)
        char_frequency = [[0] * 26 for _ in range(word_length)]

        # Step 1: Calculate frequency of each character at every index in "words".
        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1

        # Step 2: Initialize two DP arrays: prev_count and curr_count.
        prev_count = [0] * (target_length + 1)
        curr_count = [0] * (target_length + 1)

        # Base case: There is one way to form an empty target string.
        prev_count[0] = 1

        # Step 3: Fill the DP arrays.
        for curr_word in range(1, word_length + 1):
            curr_count = prev_count.copy()
            for curr_target in range(1, target_length + 1):
                cur_pos = ord(target[curr_target - 1]) - ord("a")

                # If characters match, add the number of ways.
                curr_count[curr_target] += (
                    char_frequency[curr_word - 1][cur_pos]
                    * prev_count[curr_target - 1]
                ) % MOD
                curr_count[curr_target] %= MOD

            # Move current row to previous row for the next iteration.
            prev_count = curr_count.copy()

        # Step 4: The result is in prev[target_length].
        return curr_count[target_length]
