import art
import random

def number_guesser(num):
    global counter
    if num == rand_num:
        print(f"You guessed correctly in {counter} chances. ")
    elif num > rand_num:
        print("Too high!")
        counter += 1
    elif num < rand_num:
        print("Too low!")
        counter += 1

rand_num = random.randint(0, 101)
counter = 0

print(art.logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chances = 0

if difficulty == "easy":
    chances = 10
else:
    chances = 5

print(f"You have {chances} attempts to guess the number.")

while counter < chances:
    guess = int(input("Make a guess: "))
    number_guesser(guess)
    if counter == chances:
        print(f"You lose!. Correct number was {rand_num}")
        break