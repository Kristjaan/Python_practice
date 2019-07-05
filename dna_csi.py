#!/usr/bin/env python3

# Bonus homework 11.4: Forensics program

with open('dna.txt', 'r') as file:
    dna = file.read()

hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_blonde = "TTAGCTATCGC"

face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

eyes_blue = "TTGTGGTGGC"
eyes_green = "GGGAGGTGGC"
eyes_brown = "AAGTAGTGAC"

female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

white = "AAAACCTCA"
black = "CGACTACAG"
asian = "CGCGGGCCG"


if female in dna and white in dna and hair_blonde in dna and eyes_blue in dna and face_oval in dna:
    print("It was Eva!")
elif female in dna and white in dna and hair_brown in dna and eyes_brown in dna and face_oval in dna:
    print("It was Larisa!")
elif male in dna and white in dna and hair_black in dna and eyes_blue in dna and face_oval in dna:
    print("It was Matej!")
else:
    print("It was Miha!")
