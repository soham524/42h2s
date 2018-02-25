#!/usr/bin/env python
import random
import sys
lives = 15
num = 0
i = 0
underscore = []
word = []
mode = raw_input("Enter easy, medium, or hard to choose the mode: ")
if mode == "easy":
	easyword = (random.choice(open("easy_mode.txt").readline().split()))
	i = 0
	while i < len(easyword):
		print ("_"), 
		i = i + 1 
elif mode == "medium":
	mediumword = (random.choice(open("medium_mode.txt").readline().split()))
	i = 0
	while i < len(mediumword):
		print ("_"), 
		i = i + 1 

elif mode == "hard":
	print "Note: The first letter of the word is uppercase."
	hardword = (random.choice(open("hard_mode.txt").readline().split()))
	i = 0
	word.append(hardword)
	while i < len(hardword):
		underscore.append("_")
		i = i + 1 
	print (underscore)
	while lives > 0:
			print hardword
			guess = raw_input("LETTER: ")
			if guess in hardword:
				pos = hardword.index(guess)
				underscore[pos] = guess
				print underscore
			else:
				print ("That letter is not in the word")
				print underscore
				lives = lives - 1
			i = i + 1
			print ("remaining lives: " + str(lives))
				
 		

