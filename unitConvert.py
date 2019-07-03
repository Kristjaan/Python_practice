#!/usr/bin/env python3

# Exercise 9.1: Unit converter


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calc_km_miles(km):
    miles = float(km) * 0.62137
    return miles


print("Hello! I'm a unit converter. I convert kilometers into miles.")

bool = True

while bool:
    km = input("Please enter number of kilometers: ")
    if is_number(km):
        print(calc_km_miles(km))
        for i in range(1, 4):
            another_conversion = input(
                "Do you want to do another conversion? (Y/N): ")
            if another_conversion.lower() == "y":
                break
            elif another_conversion.lower() == "n":
                bool = False
                break
            else:
                print("Input not recognized.")
                if i == 3:
                    bool = False
    else:
        print("Value not recognized. Please type a number.")
