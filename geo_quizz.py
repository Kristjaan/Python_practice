#!/usr/bin/env python3

# Bonus homework 12.3: Geography Quiz


countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb",
                    "Spain": "Madrid", "Slovenia": "Ljubljana"}


def main():
    print("Hello to the Geography quizz!")
    for key in countries_cities.keys():
        answer = input("What is the capital city of {}? ".format(key))
        if answer.lower() == countries_cities[key].lower():
            print("This is correct!")
        else:
            print("Sorry. This is wrong!")


if __name__ == "__main__":
    main()
