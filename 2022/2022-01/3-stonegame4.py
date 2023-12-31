'''
Leetcode
1510. Stone Game IV
2022-01-22
'''

import math

# try1, brute-force recursively fill look-up table bottom-up
class Solution1:

    # look-up table
    # {'number of stones': player wins on turn (if plays optimally)}
    turnWins = {'0': False, '1': True}

    @classmethod
    def simulate(self, n):

        # 1. check if n-1 is in table, if not simulate (recursion, kinda)
        if str(n - 1) not in self.turnWins:
            self.simulate(n - 1)

        # 2. determine possible moves: 1 and whole squares <= n
        # 3. check for the biggest move that leaves opponent on losing turn
        # move must 1) be > 0;  2) be a whole square;  3) not give opponent a winning turn 
        move = n
        while move > 0:
            if math.sqrt(move)%1 == 0.0: # if whole square or 1
                if not self.turnWins[str(n - move)]: # if doesn't give opponent winning turn
                    break
            move -= 1
        
        # 4. write to look-up table if turn has winning move
        if move > 0:
            self.turnWins[str(n)] = True
        else:
            self.turnWins[str(n)] = False


    @classmethod
    def winnerSquareGame(self, n):
        # check look-up table or populate if empty
        if str(n) not in self.turnWins:
            self.simulate(n)
        return self.turnWins[str(n)]



# refactored Solution1, removed simulation() function
class Solution2:

    # look-up table
    # {'number of stones left': player wins on turn (if plays optimally)}
    turnWins = {'0': False, '1': True}

    @classmethod
    def winnerSquareGame(self, n):
        # 0. check look-up table or populate if empty
        if str(n) not in self.turnWins:

            # 1. check if n-1 is in table, if not simulate (recursion, kinda)
            if str(n - 1) not in self.turnWins:
                self.turnWins[str(n - 1)] = self.winnerSquareGame(n - 1)

            # 2. determine possible moves: 1 and whole squares <= n
            # 3. check for the biggest move that leaves opponent on losing turn
            # move must 1) be > 0;  2) be a whole square;  3) not give opponent a winning turn 
            move = n
            while move > 0:
                if math.sqrt(move)%1 == 0.0: # if whole square or 1
                    if not self.turnWins[str(n - move)]: # if doesn't give opponent winning turn
                        break # found optimal move
                move -= 1
            
            # 4. write to look-up table if turn has winning move
            if move > 0:
                self.turnWins[str(n)] = True
            else:
                self.turnWins[str(n)] = False

        return self.turnWins[str(n)]



# no recursion
# Accepted
class Solution3:

    # look-up table
    # {'number of stones left': player wins on turn (if plays optimally)}
    turnWins = {'0': False, '1': True}

    @classmethod
    def winnerSquareGame(self, n):
        
        # 0. check look-up table or fill if empty
        if str(n) not in self.turnWins:

            # fill table from where it ends (len(table)) to n
            for i in range(len(self.turnWins), n + 1):
                
                c = 1 # counter
                move = c**2 # valid moves are whole squares (1 included)

                while move <= i:
                    if not self.turnWins[str(i - move)]: # if doesn't give opponent winning turn 
                        break # win is possible
                    c += 1
                    move = c**2

                self.turnWins[str(i)] = move <= i # True if move is valid

        return self.turnWins[str(n)]



# Accepted
# better time
# vastly better memory usage
class Solution4:

    # look-up table
    # losingTurns[no. of stones = n] = 0-losing turn / 1-winning
    losingTurns = [0, 1, 0, 1, 1]

    @classmethod
    def winnerSquareGame(self, n):
        
        # check if look-up table isn't filled enough
        if len(self.losingTurns) <= n:

            # fill table from where it ends to n
            for i in range(len(self.losingTurns), n + 1):
                
                c = 1 # counter
                move = c**2 # valid moves are whole squares (1 included)

                while move <= i:
                    if self.losingTurns[i - move] == 0: # if gives opponent losing turn 
                        break # win is possible
                    c += 1
                    move = c**2

                if move > i:
                    self.losingTurns.append(0) # turn has no winning moves
                else:
                    self.losingTurns.append(1)

        if self.losingTurns[n] == 0:
            return False
        else:
            return True



tests = [
    1,
    2,
    3,
    4,
    # 5,
    # 10,
    # 100,
    # 101,
    # 9347,
    # 1000,
    # 10001,
    # 100000
]
# tests = [ x for x in range(1, 21)]

for test in tests:
    print('test:', test, '\t out:', Solution4.winnerSquareGame(test))
