'''
Leetcode
875. Koko Eating Bananas
2022-01-20
'''


import math

class Solution:
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
    
    
    # more kinda bruteforce
    def minEatingSpeed(self, piles, h):
        
        def checkSpeed(k):
            hours = 0
            for i in range(len(piles)):
                time = piles[i] / k
                hours += math.ceil(time)
            if hours <= h:
                return True
            else:
                return False
        
        piles.sort(reverse=True)
        speed = piles[0]

        while checkSpeed(speed - 1):
            speed -= 1

        return speed
        
        
    # binary search but with sorting of array
    def test(self, piles, h):
        
        def checkSpeed(k):
            hours = 0
            for i in range(len(piles)):
                time = piles[i] / k
                hours += math.ceil(time)
            if hours <= h:
                return True
            else:
                return False
                
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        
        piles.sort(reverse=True)

        # find range for search
        start = None
        for i in range(1, len(piles)):
            if not checkSpeed(piles[i]):
                start = piles[i - 1]
                end = piles[i]
                break
        if not start:
            start = piles[-1]
            end = 0
        
        # binary search in range
        while start - end != 1:
            mid = round((start + end) / 2)
            print(f's-{start}, m-{mid}, e-{end}')
            if checkSpeed(mid):
                start = mid
            else:
                end = mid
            print(f'--> s-{start}, e-{end}')

        return start
        
        
    
    # binary search (pure)
    # Accepted
    def testbs(self, piles, h):
    
        start = 1        # min value
        end = 10 ** 9    # max value
        
        while start <= end:
        
            mid = round((start + end) / 2)  # speed
            
            hours = sum( math.ceil(pile / mid) for pile in piles )
            
            if hours > h:
                start = mid + 1
            else:
                end = mid - 1
                
        return start



class Test:
    def __init__(self, piles, h, res):
        self.piles = piles
        self.h = h
        self.res = res

submit = Solution()

tests = [
    Test([3,6,7,11], 8, 4),
    Test([30,11,23,4,20], 5, 30),
    Test([30,11,23,4,20], 6, 23),
    Test([5,4,3],20,1),
    Test([312884470],312884469,2)

]

for t in tests:
    print(f'\nTesting {t.piles}, h = {t.h}, expect {t.res}')
    print('Output: ' + str(submit.testbs(t.piles, t.h)))
