'''
Leetcode
421. Maximum XOR of Two Numbers in an Array (medium)
2022-01-27
'''

from typing import List


# Solution #1
# bruteforce
# time - O(n**2)
# space - O(1)
class Solution:
    def findMaximumXOR(self, nums):
        max = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i] ^ nums[j]
                if x > max: max = x
        return max



# Solution #2 
#
# Time Limit Exceeded :(
#
# biggest XOR for N is such M, that thir bits are inverted:
#   5:      00101
#   10:     01010
#   5^10:   01111
# we use trie data structure
# to store bit representations of nums in array
# then for each num in array we figure out its bit-invertion and
# find it (or the closest to it) in trie

# binary trie
class BinTrie:
    def __init__(self):
        self.node = {} # root node

    def to_bits(self, num):
        return f'{num:031b}'

    def add(self, number):
        curr = self.node
        bitNum = self.to_bits(number)
        for bit in bitNum:
            if bit not in curr:
                curr[bit] = {} # create new node
            curr = curr[bit]

    def find(self, number):
        # invert number to bit-string
        # 5 -> '...00101' -> '...11010'
        inverted = ''
        for c in self.to_bits(number):
            inverted += str( int(c) ^ 1 )

        # find closest to inverted in trie
        curr = self.node
        res = ''
        for bit in inverted:
            # Example: if bit is '0', then
            # if current node has '0' as its branch (i.e. key in dict) 
            #   -> go that way and store '0' to result
            # if not -> go the other way (0^1=1 / 1^1=0) and store '1' to result
            go = bit if bit in curr else str( int(bit) ^ 1 )
            res += go
            curr = curr[go]
        return int(res, 2)

class Solution2:
    def findMaximumXOR(self, nums):
        trie = BinTrie()
        for n in nums:
            trie.add(n)
        max = 0
        for n in nums:
            xor = n ^ trie.find(n)
            if xor > max: max = xor
        return max



# Solution #3
# stolen from @shivkj001
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/1722780/Python-Clean-and-documented-code
class Solution3:
    def findMaximumXOR(self, nums: List[int]) -> int:
        m, mask = 0, 0
        for i in range(32)[::-1]:
            mask |= 1 << i
            prefixes = {n & mask for n in nums}
            tmp = m | (1 << i)
            if any(prefix ^ tmp in prefixes for prefix in prefixes):
                m = tmp
        return m




'''
### raw solution2 ###

class BinTrieNode:
    def __init__(self):
        # self.val = None
        # self.zero = None
        # self.z = None
        # self.o = None
        # self.one = None
        # self.depth = 0
        self.children = {}


class BinTrie:
    def __init__(self):
        self.root = BinTrieNode()

    def to_bits(self, num):
        return f'{num:031b}'

    def invert_bin(self, num):
        inverted = ''
        for c in self.to_bits(num):
            inverted += str( int(c) ^ 1 )
        return int(inverted, 2)


    def add(self, number):

        bitNum = self.to_bits(number)

        curr = self.root
        
        for bit in bitNum:
            
            ### try4
            if bit not in curr.children:
                curr.children[bit] = BinTrieNode()
            curr = curr.children[bit]
            
            
            ### try3
            # if bit == '0':
            #     if curr.z == None:
            #         new = BinTrieNode()
            #         new.depth = curr.depth + 1
            #         curr.z = new
            #     curr = curr.z
            # else:
            #     if curr.o == None:
            #         new = BinTrieNode()
            #         new.depth = curr.depth + 1
            #         curr.o = new
            #     curr = curr.o

            ### try2
            # if bit not in curr.children:
            #     new_node = BinTrieNode()
            #     new_node.depth = curr.depth + 1
            #     curr.children[bit] = new_node
            # curr = curr.children[bit]

            ### try1
            # newNode = TrieNode()
            # newNode.depth = prev.depth + 1
            # if bit == '0':
            #     if prev.zero == None:
            #         prev.zero = newNode
            #     else:
            #         pass
            # else:
            #     if prev.one == None:
            #         prev.one = newNode
            # prev = newNode
        
        # curr.val = number
        
        # print(f'added: {number} -> {bitNum}')
        return
    

    def find(self, number):
        # find exact or closest value
        
        # print(f'find {number} {self.to_bits(number)} -> need ', end='')

        number = self.invert_bin(number)
        bitNum = self.to_bits(number)
        
        # print(f'{number} {bitNum} -> ', end='')
        
        curr = self.root
        res = ''
        for bit in bitNum:
            go = bit if bit in curr.children else str(int(bit) ^ 1)
            res += go
            curr = curr.children[go]

            ### try1
            # if bit == '0':
            #     if curr.z != None:
            #         curr = curr.z
            #     else:
            #         curr = curr.o
            # else:
            #     if curr.o != None:
            #         curr = curr.o
            #     else:
            #         curr = curr.z

        # print(f'found: {curr.val} {self.to_bits(curr.val)}')
        # return curr.val
        return int(res, 2)

class Solution2:
    # using trie

    def findMaximumXOR(self, nums):
        
        trie = BinTrie()
        for n in nums:
            trie.add(n)
        
        max = 0
        for n in nums:
            xor = n ^ trie.find(n)
            if xor > max: max = xor

        return max
'''





#################################################
#
#                    TESTS
#
#################################################

tests = [
    ([3,10,5,25,2,8], 28),
    ([14,70,53,83,49,91,36,80,92,51,66,70], 127)
]

solution = Solution3()

for test in tests:
    print('test:', test[0])
    out = solution.findMaximumXOR(test[0])
    print('out: ', out, '\texpect:', test[1], '\t->', out == test[1])
