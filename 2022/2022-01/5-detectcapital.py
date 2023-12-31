'''
Leetcode
520. Detect Capital
2022-01-24
'''

class Solution:

    def detectCapitalUse(self, word):
        # right usage of capitals:
        # 1) all letters are capitals
        # 2) all letters are not capitals
        # 3) only first letter is capital

        # safety check
        if len(word) < 1 or not word.isalpha():
            return False
        
        # 0 - all single letter words are valid
        elif len(word) == 1:
            return True

        # 2 - all not capitals
        elif word[0].islower():
            for i in range(1, len(word)):
                if not word[i].islower():
                    return False
            return True
        
        else:

            # 1 - all letters are capital
            if word[1].isupper():
                for i in range(2, len(word)):
                    if not word[i].isupper():
                        return False
                return True

            # 3 - only the first is capital
            else:
                for i in range(1, len(word)):
                    if not word[i].islower():
                        return False
                return True

            

# taken from comments on Leetcode
class Solution2:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()
        
tests = [
    'a',
    'A',
    'aa',
    'AA',
    'Aa',
    'aA',
    'USA',
    'FlaG',
    'GHGJFi',
    'asdsdfwR',
    '1',
    '      ',
    ''
]

for test in tests:
    print('test:', test, '\tout:', Solution2().detectCapitalUse(test))