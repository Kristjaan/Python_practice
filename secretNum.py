#!/usr/bin/env python3

#Homework 7.2: Guess the secret number

import random

secret = random.randint(1,20)

print("Welcome to Guess the secret number!\nI'm thinking of a number between 1 and 20.")

#Let the player guess 6 times
for guessesTaken in range(1, 7):
    guessesLeft = 7 - guessesTaken
    print("You have " + str(guessesLeft) + " guess(es) left.")
    guess = int(input("Take a guess: "))
    if guess >= 1 and guess <= 20:
        if guess < secret:
            print("The number you guessed is too low.")
        elif guess > secret:
            print("The number you guessed is too high.")
        else:
            print("That's right! The number is " + str(secret) + "!")
            break
    else:
        print ("I'm thinking of a number BETWEEN 1 and 20!")

if guess != secret:
    print ("Sorry. The number I was thinking of was: " + str(secret))
