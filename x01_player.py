#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  pChoice = str(input("Make your choice, enter \"Rock\", \"Paper\" or \"Scissors\": "))
  if pChoice == "Rock":
    return 0
  elif pChoice == "Paper":
    return 1
  elif pChoice == "Scissors":
    return 2
  else:
    print("Invalid Input")


if __name__ == "__main__":
  player = playerChoice()
  print(player)
