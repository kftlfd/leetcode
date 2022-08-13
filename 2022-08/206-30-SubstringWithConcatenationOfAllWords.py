"""
Leetcode
30. Substring with Concatenation of All Words (hard)
2022-08-13

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
"""

from typing import List


# leetcode solution, Approach 1: Check All Indices Using a Hash Table
# Runtime: 928 ms, faster than 39.03% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 14.3 MB, less than 16.18% of Python3 online submissions for Substring with Concatenation of All Words.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j: j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer


# leetcode solution, Approach 2: Sliding Window
# Runtime: 79 ms, faster than 97.63% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 14.2 MB, less than 38.75% of Python3 online submissions for Substring with Concatenation of All Words.
class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right: right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length  # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left: left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer


s = Solution()
tests = [
    ("barfoothefoobarman", ["foo", "bar"]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
    ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
]
for s, words in tests:
    print(t)
    print(s.findSubstring(s, words))
    print()
