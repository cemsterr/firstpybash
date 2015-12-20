#!/usr/bin/env python
import random

with open('aydin.txt', 'r') as f: # reads txt file that contains the sentences to print
	output = f.read() 			  # text stored in a variable

outputList = output.split("\n") # text splitted into sentences, as read in the file
index = random.randrange(0, len(outputList)) # choose a random sentence to print
print(outputList[index]) # print the sentence of the day
