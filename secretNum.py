#!/usr/bin/env python3

# Homework 7.2: Guess the secret number

import random
import datetime
import json


def get_score_list():
    with open("score.txt", "r") as score_file:
        global score_list
        score_list = json.loads(score_file.read())
        return score_list


def get_high_score():
    print("Top scores:")
    score_list_sorted = sorted(score_list, key=lambda kv: kv['attempts'])[:3]
    for score_dict in score_list_sorted:
        print("Player {0}: {1} attempts on {2} with secret number {3}.".format(score_dict.get(
            "name"), str(score_dict.get("attempts")), score_dict.get("date"), str(score_dict.get("secret"))))


def play_game(difficulty):
    secret = random.randint(1, 20)
    attempts = 0
    name = input("Who is playing?: ")
    print("I'm thinking of a number between 1 and 20.")

    # Let the player guess 6 times
    for guessesTaken in range(1, 7):
        guessesLeft = 7 - guessesTaken
        attempts += 1
        print("You have " + str(guessesLeft) + " guess(es) left.")
        guess = int(input("Take a guess: "))
        if guess >= 1 and guess <= 20:
            if guess == secret:
                print("That's right! The number is " + str(secret) + "!")
                score_list.append({"attempts": attempts, "date": str(
                    datetime.datetime.now()), "name": name, "secret": secret})
                with open("score.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                break
            elif guess < secret and difficulty == "easy":
                print("The number you guessed is too low.")
            elif guess > secret and difficulty == "easy":
                print("The number you guessed is too high.")
            else:
                print("You're guess is not correct.")
        else:
            print("I'm thinking of a number BETWEEN 1 and 20!")

    if guess != secret:
        print("Sorry. The number I was thinking of was: " + str(secret))


def main():
    wrong = 0
    while wrong < 3:
        get_score_list()
        print("Welcome to Guess the secret number!")
        selection = input(
            "Would you like to A) play a new game, B) see the best scores, or C) quit?")
        if selection.lower() == "a":
            difficulty = input("Which difficulty do you want to play? A) Easy, or B) Hard")
            if difficulty.lower() == "a":
                play_game("easy")
            elif difficulty.lower() == "b":
                play_game("hard")
            else:
                print("Wrong input.")
            wrong = 0
        elif selection.lower() == "b":
            get_high_score()
            wrong = 0
        elif selection.lower() == "c":
            break
        else:
            print("Input not recognized.")
            wrong += 1


if __name__ == "__main__":
    main()
