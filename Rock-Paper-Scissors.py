# Test-v1

#This is a standard Rock, Paper, Scissors game. It'll be played against computer.

#Import the random module so that computer can randomly get a choice.
import random

def get_choices():
  player_choce = input("Enter a choice (rock,paper,scissors):")
  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choce, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "scissors":
      return "Scissors cut the paper! You loss."
    else:
      return "Paper covers rock! You win!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cut the paper! You win!"
    else:
      return "Rock smashes scissors! You loss."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print (result)