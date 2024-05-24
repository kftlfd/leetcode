"""
Leetcode
1255. Maximum Score Words Formed by Letters
Hard
2024-05-24

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.

Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.

 

Constraints:

    1 <= words.length <= 14
    1 <= words[i].length <= 15
    1 <= letters.length <= 100
    letters[i].length == 1
    score.length == 26
    0 <= score[i] <= 10
    words[i], letters[i] contains only lower case English letters.

Hints:
- Note that words.length is small. This means you can iterate over every subset of words (2^N).    
"""

from typing import List


class Solution:
    """
    Runtime: 51 ms, faster than 57.14% of Python3 online submissions for Maximum Score Words Formed by Letters.
    Memory Usage: 16.7 MB, less than 53.06% of Python3 online submissions for Maximum Score Words Formed by Letters.
    """

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_cnt = [0] * 26
        for c in letters:
            letters_cnt[ord(c) - ord('a')] += 1

        max_score = [0]

        def dfs(i: int, pick: bool, cur_cnt: List[int]):
            if i >= len(words):
                return

            if pick:
                for c in words[i]:
                    cur_cnt[ord(c) - ord('a')] += 1

                # can't pick this word
                if any(n > available for n, available in zip(cur_cnt, letters_cnt)):
                    for c in words[i]:
                        cur_cnt[ord(c) - ord('a')] -= 1
                    return

                # update max_score
                cur_score = sum(cnt * val for cnt, val in zip(cur_cnt, score))
                max_score[0] = max(max_score[0], cur_score)

            dfs(i + 1, True, cur_cnt)
            dfs(i + 1, False, cur_cnt)

            if pick:
                for c in words[i]:
                    cur_cnt[ord(c) - ord('a')] -= 1

        dfs(-1, False, [0] * 26)

        return max_score[0]


class Solution1:
    """
    leetcode solution 1: Iterative Loop for Every Subset
    Runtime: 367 ms, faster than 5.89% of Python3 online submissions for Maximum Score Words Formed by Letters.
    Memory Usage: 16.5 MB, less than 99.55% of Python3 online submissions for Maximum Score Words Formed by Letters.
    """

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        # Count how many times each letter occurs
        freq = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        # Calculate score of subset
        def subset_score(subset_letters, score, freq):
            total_score = 0
            for c in range(26):
                total_score += subset_letters[c] * score[c]
                # Check if we have enough of each letter to build this subset of words
                if subset_letters[c] > freq[c]:
                    return 0
            return total_score

        max_score = 0
        # Iterate over every subset of words
        subset_letters = {}
        for mask in range(1 << W):
            # Reset the subset_letters map
            subset_letters = [0 for i in range(26)]
            # Find words in this subset
            for i in range(W):
                if (mask & (1 << i)) > 0:
                    # Count the letters in this word
                    L = len(words[i])
                    for j in range(L):
                        subset_letters[ord(words[i][j]) - 97] += 1
            # Calculate score of subset
            max_score = max(max_score, subset_score(
                subset_letters, score, freq))
        # Return max_score as the result
        return max_score


class Solution2:
    """
    leetcode solution 2: Backtracking
    Runtime: 51 ms, faster than 57.14% of Python3 online submissions for Maximum Score Words Formed by Letters.
    Memory Usage: 16.4 MB, less than 99.55% of Python3 online submissions for Maximum Score Words Formed by Letters.
    """

    max_score = 0

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        # Count how many times each letter occurs
        self.max_score = 0
        freq = [0 for i in range(26)]
        subset_letters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        # Check if adding this word exceeds the frequency of any letter
        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            return True

        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                # If all words have been iterated, check the score of this subset
                self.max_score = max(self.max_score, total_score)
                return
            # Not adding words[w] to the current subset
            check(w - 1, words, score, subset_letters, total_score)
            # Adding words[w] to the current subset
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]

            if is_valid_word(subset_letters):
                # Consider the next word if this subset is still valid
                check(w - 1, words, score, subset_letters, total_score)

            # Rollback effects of this word
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]

        check(W - 1, words, score, subset_letters, 0)
        # Return max_score as the result
        return self.max_score


s = Solution()
tests = [
    ((
        ["xxxz", "ax", "bx", "cx"],
        ["z", "a", "b", "c", "x", "x", "x"],
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    ),
        27),
]
for inp, exp in tests:
    res = s.maxScoreWords(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
