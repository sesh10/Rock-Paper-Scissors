# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):
    # opponent_history.append(prev_play)

    # guess = "R"
    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    # return guess
  

  opponent_history.append(prev_play)
  mat = ['R', 'P', 'S']
  guess = random.choice(mat)

  if len(opponent_history) > 1:
    if opponent_history[-1] == 'R':
      guess = random.choices(mat, [30, 70, 40], k=1)
    elif opponent_history[-1] == 'S':
      guess = random.choices(mat, [80, 40, 30], k=1)
    elif opponent_history[-1] == 'P':
      guess = random.choices(mat, [40, 20, 80], k=1)

  return guess[0]



