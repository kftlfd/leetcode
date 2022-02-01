'''
Leetcode
134. Gas Station
2022-01-21
'''

class CanCompleteCircuit:

    @classmethod
    # improved after try2 failed
    # Accepted
    def try1(self, gas, cost):
    
        print('gas: ', gas)
        print('cost:', cost)
        
        # prepare variables
        n = len(gas)
        tank = 0        
        startPoint = 0
        startSet = False

        for i in range(n * 2):
            
            print(f'{i}. station {i%n}:  tank-{tank}  gas-{gas[i%n]}  cost-{cost[i%n]}', end='  ')
            
            tank = tank + gas[i%n] - cost[i%n]

            # check if can drive to next station
            if tank >= 0:
                print('yes', end='  ')
                
                # remember start point
                if not startSet:
                    print('set startPoint', end='  ')
                    startPoint = i
                    startSet = True
                
                if i == startPoint + n - 1:
                    print('full circle possible')
                    return startPoint
                
                print('')

            # if can not, then previous stations and current one are not a vaible start points
            else:
                print('no ', end='  ')

                # if on the last station
                if i >= n - 1:
                    print('checked all stations')
                    return -1

                # reset variables
                print('resetting')
                tank = 0
                startSet = False
                
        return -1


    @classmethod
    # brute force every station
    # time limit exceeded after 34/35 cases
    def try2(self, gas, cost):

        n = len(gas)

        def checkStation(start):
            tank = 0
            print(f'station {start}')
            for i in range(start, start + n):
                print(f'{tank} + {gas[i%n]} - {cost[i%n]} -> ', end='')
                tank = tank + gas[i%n] - cost[i%n]
                print(f'{tank} ', end='')
                if tank < 0:
                    print('no')
                    return False
                print('yes')
            return True

        for i in range(n):
            if checkStation(i):
                return i
        
        return -1



    @classmethod
    def solution1(self, gas, cost):
        '''
        by @hi-malik
        https://leetcode.com/problems/gas-station/discuss/1706142/JavaC++Python-An-explanation-that-ever-EXISTS-till-now!!!!
        '''

        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start



tests = [
    ( [1,2,3,4,5], [3,4,5,1,2] ),
    ( [2,3,4], [3,4,3] ),
    ( [5,1,2,3,4], [4,4,1,5,1] ),
    ( [5], [4] )
]

for test in tests:
    print('\ntest:', test)
    print('out: ', CanCompleteCircuit.solution1(*test), '\n')
