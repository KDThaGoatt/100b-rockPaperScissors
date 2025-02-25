#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import playerChoice
from x02_computer import computerChoice
from x03_winner import playerWins

while True:
  player = playerChoice()
  comp = computerChoice()
  winner = playerWins(comp, player)

  if comp == 0:
    print("\033[1mOpponent chose rock\033[0m")
  elif comp == 1:
    print("\033[1mOpponent chose paper\033[0m")
  else:
    print("\033[1mOpponent chose scissors\033[0m")

  if winner == -1:
    print("\033[0;31mYou Lost\033[0m")
  elif winner == 0:
    print("\033[1;33mDraw\033[0m")
  else:
    print("\033[0;32mYou Win!\033[0m")


  if __name__ == "__main__":
    pass

