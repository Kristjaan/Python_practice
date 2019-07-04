#!/usr/bin/env python3

# Homework 7.2: Guess the secret number

import random
import datetime
import json

secret = random.randint(1, 20)
attempts = 0
score = {}

name = input("Who is playing?: ")

print("Top scores:")

with open("score.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list_sorted = sorted(score_list, key=lambda kv: kv['attempts'])[:3]
    for score_dict in score_list_sorted:
        print("Player {0}: {1} attempts on {2} with secret number {3}.".format(score_dict.get(
            "name"), str(score_dict.get("attempts")), score_dict.get("date"), str(score_dict.get("secret"))))


print("Welcome to Guess the secret number!\nI'm thinking of a number between 1 and 20.")

# Let the player guess 6 times
for guessesTaken in range(1, 7):
    guessesLeft = 7 - guessesTaken
    attempts += 1
    print("You have " + str(guessesLeft) + " guess(es) left.")
    guess = int(input("Take a guess: "))
    if guess >= 1 and guess <= 20:
        if guess < secret:
            print("The number you guessed is too low.")
        elif guess > secret:
            print("The number you guessed is too high.")
        else:
            print("That's right! The number is " + str(secret) + "!")
            score_list.append({"attempts": attempts, "date": str(
                datetime.datetime.now()), "name": name, "secret": secret})
            with open("score.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break
    else:
        print("I'm thinking of a number BETWEEN 1 and 20!")

if guess != secret:
    print("Sorry. The number I was thinking of was: " + str(secret))

for key, value in score.items():
    print(key, value, end=" ")
