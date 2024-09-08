from random import randint
Easy = 10
Hard = 5
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def difficulty():
  level = input("'easy' or 'hard': ")
  if level == "easy":
    return Easy
  else:
    return Hard
def game():
  print("Welcome!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  #print(f"Correct answer is {answer}")

  turns = difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining.")
    guess = int(input("Your guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You lost.")
    elif guess != answer:
      print("Guess again.")
game()
