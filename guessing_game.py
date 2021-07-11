#!/usr/bin/env python3

from random import randint

answer = randint(1, 1000)
guess = 0
tries = 0

print("I am thinking of a number between 1 and 1000")

while guess != answer:
	try:
		guess = int(input("Enter your guess: "))

		tries += 1

		if guess < answer:
			print("Too Low")
		elif guess > answer:
			print("Too High")
		else:
			print("Correct! You Win!")
			print(f"It took you {tries} tries.")	

	except ValueError:
		print("[ERROR]: Enter a valid number.")
