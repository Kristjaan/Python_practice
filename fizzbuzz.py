#!usr/bin/env python3

# Homework 9.2: FizzBuzz

num = int(input("Select a number between 1 and 100: "))

for i in range(1, num+1):
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
