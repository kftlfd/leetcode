'''
Leetcode
1291. Sequential Digits
2022-01-23
'''

class Soultion1:
    
    @classmethod
    def sequentialDigits(self, low, high):
        
        n = '123456789'
        snums = []
        sLenPrev = len(snums)

        def addNextDigit(n):
            nextDigit = (n % 10 + 1) % 10
            if nextDigit == 0:
                return -1
            return n * 10 + nextDigit

        # generate all sequential digit numbers
        for i in range(2, 10):
            # go through all possible i-digit numbers
            # i = number of digits, from 2 to 9

            if i == 2:
                # first pass, create 2-digit numbers from 'n'
                for j in range(len(n) - 1):
                    num = addNextDigit(int(n[j]))
                    if num != -1:
                        snums.append(num)
                    # print(snums)
            
            else:
                # next passes, use generated numbers from [snums] to generate next-digit numbers
                sLenNew = len(snums)
                for j in range(sLenPrev, len(snums)):
                    if len(str(snums[j])) == i - 1:
                        num = addNextDigit(snums[j])
                        if num != -1:
                            snums.append(num)
                    # print(snums)
                sLenPrev = sLenNew
        
        # check for snums in range low-high
        out = []
        for i in range(len(snums)):
            if snums[i] >= low and snums[i] <= high:
                out.append(snums[i])
        
        # print(snums)
        # print(out)
        return out



# pre-calculated, lol
# somehow, runtime is worse than in Soution 1
class Soultion2:
    
    @classmethod
    def sequentialDigits(self, low, high):
        
        snums = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]

        out = []
        for i in range(len(snums)):
            if snums[i] >= low and snums[i] <= high:
                out.append(snums[i])
        
        return out



tests = [
    [100, 300],
    [1000, 13000],
    [10, 10],
    [100000000, 1000000000],
    [10, 1000000000]
]

for test in tests:
    print('test:', test)
    print('out: ', Soultion2.sequentialDigits(test[0], test[1]))