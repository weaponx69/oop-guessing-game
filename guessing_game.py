import random

class GuessingGame():
    def __init__(self, correct_number):
        self.correct_number = correct_number
        self.is_solved = False

    def is_solved(self):
       # Renamed to is_solved to avoid conflict with the attribute
       return self.is_solved
    
    def guess_results(self, current_guess):
       return self.is_solved()


# create a new random number
game = GuessingGame(random.randint(1,100))
# These variables are unused in the loop but were kept for completeness
previous_guess  = 0
previous_result = 0


print('HEY PLAYER1 WELCOME TO MY NUMBER GUESSING GAME')
player_name = input("What is your name: ")
print(f'Welcome {player_name}! I hope you are ready to play!')


while game.is_solved is False:
  current_guess = int(input("pick a number: "))
  if current_guess != game.correct_number:
    print(f"Oops! Your last guess ({current_guess}) was wrong.  Correct answer: {game.correct_number}.")
    game.is_solved = False
  else:
    game.is_solved = True
    print(f"{player_name} that was correct!  Thank you for playing.")
