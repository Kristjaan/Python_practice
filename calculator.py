#!/usr/bin/env python3

#Homework 7.2: Calculator

print("Hello! I'm a basic calculator!")
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

arithmetic = input("Please enter an arithmetic operator (+,-,*,/): ")

if arithmetic == "+":
    result = num1 + num2
    print(result)
elif arithmetic == "-":
    result = num1 - num2
    print(result)
elif arithmetic == "*":
    result = num1 * num2
    print(result)
elif arithmetic == "/":
    result = num1 / num2
    print(result)
'''
elif arithmetic == "**":
    result = num1 ** num2
    print(result)
'''
else:
    print("I don't recognize the arithmetic operator or you have to use a more advanced calculator.")
