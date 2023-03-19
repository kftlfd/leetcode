"""
Leetcode
211. Design Add and Search Words Data Structure (medium)
2023-03-19

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.chars = {}


class WordDictionary:
    """
    Runtime: 9532 ms, faster than 68.02% of Python3 online submissions for Design Add and Search Words Data Structure.
    Memory Usage: 78.3 MB, less than 25.48% of Python3 online submissions for Design Add and Search Words Data Structure.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TrieNode()
            curr = curr.chars[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        q = [self.root]

        for c in word:

            if not q:
                return False

            for _ in range(len(q)):
                node = q.pop(0)
                if c == '.':
                    q += node.chars.values()
                elif c in node.chars:
                    q.append(node.chars[c])

        return any(node.is_word for node in q)
