'''
Leetcode
211. Design Add and Search Words Data Structure (medium)
2022-01-28
'''

# Instructions:

# Implement the WordDictionary class:
#  - WordDictionary() Initializes the object.
#  - void addWord(word) Adds word to the data structure, it can be matched later.
#  - bool search(word) Returns true if there is any string in the data structure that 
#    matches word or false otherwise. word may contain dots '.' where 
#    dots can be matched with any letter.

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Solution accepted
# bad time, ok space efficiency

class Node:
    def __init__(self):
        self.is_word = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next: node.next[c] = Node()
            node = node.next[c]
        node.is_word = True
        return f'added: {word}'

    def search(self, word: str, **kwargs) -> bool:
        
        if kwargs: node = kwargs['node']
        else: node = self.root

        og_word= word
        word = [char for char in word]
            
        for c in og_word:
            
            if c in node.next: 
                node = node.next[c]
            
            elif c == '.':
                # remove '.' from word
                word.pop(0)
                # get every next node
                branches = [node.next[c] for c in node.next]
                # search (recursively) for word in every branch
                results = [self.search(word, node=b) for b in branches]
                return any(results)
            
            else: return False
            
            word.pop(0)

        return node.is_word
        


add =    ["bad", "dad", "mad"]
search = ["pad", "bad", ".ad", "b..", "ba"]

obj = WordDictionary()

for word in add:
    print( obj.addWord(word) )

for word in search:
    print( f'search "{word}":', obj.search(word) )
