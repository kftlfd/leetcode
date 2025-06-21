"""
Leetcode
2025-06-21
3085. Minimum Deletions to Make String K-Special
Medium

You are given a string word and an integer k.

We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

Here, freq(x) denotes the

of the character x in word, and |y| denotes the absolute value of y.

Return the minimum number of characters you need to delete to make word k-special.

 

Example 1:

Input: word = "aabcaba", k = 0

Output: 3

Explanation: We can make word 0-special by deleting 2 occurrences of "a" and 1 occurrence of "c". Therefore, word becomes equal to "baba" where freq('a') == freq('b') == 2.

Example 2:

Input: word = "dabdcbdcdcd", k = 2

Output: 2

Explanation: We can make word 2-special by deleting 1 occurrence of "a" and 1 occurrence of "d". Therefore, word becomes equal to "bdcbdcdcd" where freq('b') == 2, freq('c') == 3, and freq('d') == 4.

Example 3:

Input: word = "aaabaaa", k = 2

Output: 1

Explanation: We can make word 2-special by deleting 1 occurrence of "b". Therefore, word becomes equal to "aaaaaa" where each letter's frequency is now uniformly 6.

 

Constraints:

    1 <= word.length <= 10^5
    0 <= k <= 10^5
    word consists only of lowercase English letters.

    
Hint 1
Count the frequency of each letter.
Hint 2
Suppose we select several characters as the final answer, and let x be the character with the smallest frequency in the answer. It can be shown that out of the selected characters, the optimal solution will never delete an occurrence of character x to obtain the answer.
Hint 3
We will fix a character c and assume that it will be the character with the smallest frequency in the answer. Suppose its frequency is x.
Hint 4
Then, for every other character, we will count the number of occurrences that will be deleted. Suppose that the current character has y occurrences.
    1. If y < x, we need to delete all of them.
    2. if y > x + k, we should delete y - x - k of such character.
    3. Otherwise we don’t need to delete it.
"""


from collections import defaultdict


class Solution:
    """
    Runtime 88ms Beats 32.56%
    Memory 18.03MB Beats 70.54%
    """

    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - 97] += 1

        ans = len(word)

        for fixed_c, freq_c in enumerate(freq):
            if freq_c == 0:
                continue
            cur_ans = 0
            for other_c, freq_other in enumerate(freq):
                if other_c == fixed_c or freq_other == 0:
                    continue
                if freq_other < freq_c:
                    cur_ans += freq_other
                elif freq_other > freq_c + k:
                    cur_ans += freq_other - (freq_c + k)
                if cur_ans > ans:
                    break
            ans = min(ans, cur_ans)

        return ans


class Solution1:
    """
    leetcode solution: Hash Table + Enumeration
    Runtime 87ms Beats 33.33%
    Memory 18.22MB Beats 20.15%
    """

    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res
