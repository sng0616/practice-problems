# Project idea from http://www.pbs.org/idealab/2014/07/5-fun-programming-projects-to-help-learn-python/

# Add definitions later --> http://developer.wordnik.com/#!/libraries#python

'''
How do you lose Hangman? Too many (>6) incorrect guesses.

How do you win at Hangman? Guess all the correct letters without making >6 incorrect guesses.

What do I need to know to play Hangman? List of total guesses, number of incorrect guesses	
'''

import urllib

wordSource = "http://randomword.setgetgo.com/get.php"

#def findWord(wordSource):
WordReq = urllib.urlopen(wordSource)
randWord = WordReq.read().strip()
randWordLow = randWord.lower()
randWordLen = len(randWord)
wordList = list(randWord)
letterNo = enumerate(randWord)
empty = "_ " * randWordLen

level = raw_input("What level do you want? (Easy or Hard) " )

# Easy Level
if level == "Easy":
	while randWordLen > 10:
		WordReq = urllib.urlopen(wordSource)
		randWord = WordReq.read().strip()

# Medium Level
#if level == "Medium":	
#	while randWordLen < 7 or randWordLen > 10:
#		WordReq = urllib.urlopen(wordSource)
#		randWord = WordReq.read().strip()
		
# Hard Level
if level == "Hard":
	while randWordLen < 10:
		WordReq = urllib.urlopen(wordSource)
		randWord = WordReq.read().strip()

print randWord
print "This word has {0} letters." .format(randWordLen)
print empty



guessLett = raw_input("Guess a letter. ")[:1]
guessList = []
missedList = []
correctList = []

def checkGuess(guessLett):
	if guessLett.isalpha() == False:
		guessLett = raw_input("That was not a letter. Please guess a letter. ")[:1]
	if guessLett in guessList:
		guessLett = raw_input("You already guessed that letter. Please guess another letter. ")[:1]
	return 
	
checkGuess(guessLett)
# Function to make sure guess is a single letter
	
# What loop do I need to put all of the guessed letters in a list? 

while len(missedList) < 6:
#def is_guess_correct(guessLett):
	if guessLett.isalpha() == False:
		guessLett = raw_input("That was not a letter. Please guess a letter. ")[:1]
	if guessLett in guessList:
			guessLett = raw_input("You already guessed that letter. Please guess another letter. ")[:1]	
	if guessLett in randWord:
#		if guessLett in guessList:
#			guessLett = raw_input("You already guessed that letter. Please guess another letter. ")[:1]	
		guessList.append(guessLett)
		correctList.append(guessLett)
		if sorted(set(wordList)) == sorted(set(correctList)):
			print "The word was {0}. You won!" .format(randWord)
			break 
		else:
			for i in range(randWordLen):
				if randWord[i] in correctList:
					empty = empty[:i*2]+randWord[i]+" "+empty[(i+1)*2:]
			print empty[:randWordLen*2]
			print correctList
			print missedList
			guessLett = raw_input("Good guess. Try again. ")
	if guessLett not in randWord:
#		if guessLett.isalpha() == False:
#			guessLett = raw_input("That was not a letter. Please guess a letter. ")[:1]
#		if guessLett in guessList:
#			guessLett = raw_input("You already guessed that letter. Please guess another letter. ")[:1]	
		guessList.append(guessLett)
		missedList.append(guessLett)
		if len(missedList) == 6:
			print "The word was {0}. You lose." .format(randWord)
		else:
			for i in range(randWordLen):
				if randWord[i] in correctList:
					empty = empty[:i*2]+randWord[i]+" "+empty[(i+1)*2:]
			print empty[:randWordLen*2]
			print correctList
			print missedList
			guessLett = raw_input("No dice. Try again. ")

