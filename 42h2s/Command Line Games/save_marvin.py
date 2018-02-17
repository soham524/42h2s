#!/usr/bin/env python
import random
import sys
lives = 10 
num = 0
i = 0
underscore = []
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
	while i < len(hardword):
		#print hardword
		underscore.append("_")
		i = i + 1 
	print underscore
	while i < lives:
			guess = raw_input("LETTER: ")
			if guess in hardword:
				print underscore.replace("_", guess, hardword.index(guess))
			
			else:
				print ("_"),		
			i = i + 1
			print ("remaining lives: " + str(lives-i))
				
 		

