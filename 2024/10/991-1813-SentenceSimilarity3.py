"""
Leetcode
2024-10-06
1813. Sentence Similarity III
Medium

You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

    s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
    s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"

Output: false

Explanation:

No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

 

Constraints:

    1 <= sentence1.length, sentence2.length <= 100
    sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
    The words in sentence1 and sentence2 are separated by a single space.
"""


from collections import deque


class Solution:
    """
    Runtime: 30 ms, faster than 86.96% of Python3 online submissions for Sentence Similarity III.
    Memory Usage: 16.5 MB, less than 80.43% of Python3 online submissions for Sentence Similarity III.
    """

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')

        if len(words1) > len(words2):
            words1, words2 = words2, words1

        n = len(words1)
        if words1 == words2[:n] or words1 == words2[-n:]:
            return True

        for break_idx in range(1, n):
            left, right = words1[:break_idx], words1[break_idx:]
            if left == words2[:break_idx] and right == words2[-(n-break_idx):]:
                return True

        return False


class Solution1:
    """
    leetcode solution 1: Deque
    Runtime: 28 ms, faster than 90.37% of Python3 online submissions for Sentence Similarity III.
    Memory Usage: 16.6 MB, less than 13.04% of Python3 online submissions for Sentence Similarity III.
    """

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        deque1 = deque(sentence1.split())
        deque2 = deque(sentence2.split())
        # Compare the prefixes or beginning of the strings.
        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.popleft()
            deque2.popleft()
        # Compare the suffixes or ending of the strings.
        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop()
            deque2.pop()
        return not deque1 or not deque2


class Solution2:
    """
    leetcode solution 2: Two Pointers
    Runtime: 41 ms, faster than 17.70% of Python3 online submissions for Sentence Similarity III.
    Memory Usage: 16.7 MB, less than 13.04% of Python3 online submissions for Sentence Similarity III.
    """

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split the words in sentences and store it in a string array.
        s1_words = sentence1.split(" ")
        s2_words = sentence2.split(" ")
        start, ends1, ends2 = 0, len(s1_words) - 1, len(s2_words) - 1

        # If words in s1 are more than s2, swap them and return the answer.
        if len(s1_words) > len(s2_words):
            return self.areSentencesSimilar(sentence2, sentence1)

        # Find the maximum words matching from the beginning.
        while start < len(s1_words) and s1_words[start] == s2_words[start]:
            start += 1

        # Find the maximum words matching in the end.
        while ends1 >= 0 and s1_words[ends1] == s2_words[ends2]:
            ends1 -= 1
            ends2 -= 1

        # If i reaches the end of the array, then we return true.
        return ends1 < start
