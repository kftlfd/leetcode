"""
Leetcode
745. Prefix and Suffix Search (hard)
2022-06-18

Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

 - WordFilter(string[] words) Initializes the object with the words in the dictionary.
 - f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
"""

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)



# leetcode solution - Approach #3: Trie of Suffix Wrapped Words
# Runtime: 1367 ms, faster than 75.54% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 60.6 MB, less than 34.25% of Python3 online submissions for Prefix and Suffix Search.
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]
        


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
