#!/usr/bin/env python3.8
import random

hidden = random.randint(1,10)
bool=True
while bool:
    guess = int(input("enter your guess"))
    if guess == hidden:
        print("number guessed")
        bool=False
    elif guess < hidden:
        print("guess is too low")
    elif guess > hidden:
        print("guess is too high")
    else:
        print("guess incorrect")