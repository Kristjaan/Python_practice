#!/usr/bin/env python3

#Homework 7.1: The mood checker

mood = input("Hello!\nHow are you today?\n")

if mood.lower() == "happy":
    print("It is great to see you happy!")
elif mood.lower() == "nervous":
    print("Take a deep breath 3 times.")
elif mood.lower() == "excited":
    print("Great! Have fun! Say hello to Mike for me!")
elif mood.lower() == "sad":
    print("Get yourself together!")
elif mood.lower() == "relaxed":
    print("Keep chillin', Bro!")
else:
    print("I don't recogize this mood")
