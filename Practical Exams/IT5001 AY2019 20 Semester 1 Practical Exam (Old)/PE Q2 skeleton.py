
from pprint import pprint

print("Part 2")
psrlsdict = {0:'scissor',1:'paper',2:'rock',3:'lizard',4:'Spock'}

def psrlsWhoWin(p1move,p2move):
    return 0

def nP1Wins(p1moves,p2moves):
    return 0


p1moves = [1,2,3,0,4,4,0]
p2moves = [2,4,1,4,3,0,2]
print(nP1Wins(p1moves,p2moves))


def findWinningSeq(p1moves,p2moves):
    return [[]]

p1moves = [3,2,1]
p2moves = [1,2,3]
print(nP1Wins(p1moves,p2moves))
newp1moves = findWinningSeq(p1moves,p2moves)
print(newp1moves)
print(nP1Wins(newp1moves[0],p2moves))

p1moves = [1,2,3,0,4,4,0]
p2moves = [2,4,1,4,3,0,2]
print(nP1Wins(p1moves,p2moves))
newp1moves = findWinningSeq(p1moves,p2moves)
print(newp1moves)
print(nP1Wins(newp1moves[0],p2moves))


