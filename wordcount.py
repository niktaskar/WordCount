import pandas as pd
import re
import math
from functools import reduce
from collections import Counter

words = {} # dictionary to hold all the words and counts

test = {"hi": 1, "bye": 1}

tuplesOfWords = [] # matrix of word tuples
countOfTuples = Counter() # count of tuples

tuples = {} # should be a tuple followed by a dictionary of words associated with their counts

class WordCount:

	def __init__ (self, s):
		self.st = s
		self.words = words
		# touple should be words in the same 
		# self.tuplesOfWords = tuplesOfWords

	# METHODS IN THIS CLASS NEED TO HAVE self AS A PARAMETER
	# created tuples for each pair of word and mapped them to tuplesOfWords list
	# need to reduce them into counts of tuples that match
	# then reduce even further to (word1: [[words that follow], [counts]])
	def readInput(self):
		file = open(self.st, encoding ="utf-8")
		line = file.readline()
		word1 = ""
		word2 = ""
		word3 = ""
		totalnumwords = 0
		dictOfWords = {}
		for line in file:
			for char in line:
				# have a problem when two unwanted chars follow each other
				if(char != ' ' and char != ',' and char != '\n' and char != '.' 
					and char != ';' and char != ':' and char != '-' and char != '?'
					and char != '!' and char != '(' and char != ')' and char != '\t'
					and char != '/' and char != '' and char != '"'):
					word3 += char
					continue
				else:
					word1.lower()
					word2.lower()
					word3.lower()
					if (word3 in self.words):
						self.words[word3] += 1
						tup = (word1, word2, word3)
						tuplesOfWords.append(tup)
						countOfTuples[tup] += 1  # counts the number of times a tuple occurs
					else:
						self.words[word3] = 1
						tup = (word1, word2, word3)
						tuplesOfWords.append(tup)
						countOfTuples[tup] += 1 # counts the number of times a tuple occurs
					totalnumwords += 1	
					word1 = word2
					word2 = word3
					word3 = ""

		file.close()

		return words 

	def createDF(self):
		file = open(self.st, encoding = "utf-8")
		line = file.readline()
		word1 = ""
		word2 = ""
		word3 = ""
		for line in file:
			for char in line:
				# have a problem when two unwanted chars follow each other
				if(char != ' ' and char != ',' and char != '\n' and char != '.' 
					and char != ';' and char != ':' and char != '-' and char != '?'
					and char != '!' and char != '(' and char != ')' and char != '\t'
					and char != '/' and char != '' and char != '"'):
					word3 += char
					continue
				else:
					word1.lower()
					word2.lower()
					word3.lower()
					if (tuple([word1, word2]) in tuples):
						if(word3 in tuples[tuple([word1, word2])]):
							# print(tuples[tuple([word1, word2])])
							tuples[tuple([word1, word2])][word3] += 1
							# print("word3 in tuples")
							# print(word1 + " " + word2 + " " + word3 + " " + str(tuples[tuple([word1, word2])][word3]))
						else:
							# print("word3 not in tuples")
							tuples[tuple([word1, word2])][word3] = 1
							# print(word1 + " " + word2 + " " + word3 + " " + str(tuples[tuple([word1, word2])][word3]))
					else:
						# print("tuple not in tuples")
						tuples[tuple([word1, word2])] = {word3: 1}
						# print(word1 + " " + word2 + " " + word3 + " " + str(tuples[tuple([word1, word2])][word3]))
					word1 = word2
					word2 = word3
					word3 = ""


		# dfTraining = pd.DataFrame.from_dict(self.words, orient = "index") # word counts as a dataframe

		# newly formatted into dataframe
		arrTupCount = pd.DataFrame.from_dict(countOfTuples, orient = "index")
		print(arrTupCount)

		# PRINTS OUT THE DICTIONARY ATTACHED TO TWO WORD TUPLES
		# print(str(tuples[tuple(["of", "the"])])) 
		for tup in tuples:
			print(str(tup[0]) + " " + str(tup[1]) + " " + str(tuples[tuple([str(tup[0]), str(tup[1])])]))
			# print("hello world")
			# print(str(tup) + " " + str(tuples[tuple([str(tup[0]), str(tup[1])])]))
		return tuples

	def sigmoid(self):
		count = 0
		# tuplesDF = pd.DataFrame.from_dict(tuples, orient = "index")
		# print(tuplesDF)

		for tup in tuples:
			#prep
			# CANT ACCESS KEYS FOR DICTIONARY USING INDEX NEED ACTUAL STRINGS
			print(tup)
			for i in  tuples[tuple([str(tup[0]), str(tup[1])])].keys():	#range(0,len(tuples[tuple([str(tup[0]), str(tup[1])])])):
				print(i + " " + str(tuples[tuple([str(tup[0]), str(tup[1])])][i]))
				tuples[tuple([str(tup[0]), str(tup[1])])][i] = 1 / (1 + math.exp((-1)*(tuples[tuple([str(tup[0]), str(tup[1])])][i])))
				print(i + " " + str(tuples[tuple([str(tup[0]), str(tup[1])])]))
				# print(tup) THIS IS JUST THE TUPLE
				# print(len(tup)) THIS IS TWO
				# print(tuples[tuple([str(tup[0]), str(tup[1])])]) #PRINTS THE DICTIONARY OF THE TUPLE

		# THIS IS HOW TO ITERATE THROUGH TUPLES
		# for i in test.keys():
		# 	print(test[i])
		# print(str(math.exp(1)))


	def sigmoidDeriv(self):
		return 1

	# GOING TO READ INPUT FILE AND DETERMINE THE EXPECTED FREQUENCIES OF EACH WORD
	def readAndPredict(self, s):
		wordsInDoc = {}
		word = ""
		file = open(s, encoding = "utf-8")
		line = file.readline()
		totalnumwords = 0
		for line in file:
			for char in line:
				# have a problem when two unwanted chars follow each other
				if(char != ' ' and char != ',' and char != '\n' and char != '.' 
					and char != ';' and char != ':' and char != '-' and char != '?'
					and char != '!' and char != '(' and char != ')' and char != '\t'
					and char != '/' and char != '' and char != '"'):
					word += char
					continue
				else:
					if(word in wordsInDoc):
						wordsInDoc[word] += 1
					else:
						wordsInDoc[word] = 1
					totalnumwords += 1
					word = ""
		file.close()
		# creats a (num of words) by 1 matrix
		dfNewInput = pd.DataFrame.from_dict(self.wordsInDoc, orient = "index")
		print(dfNewInput)


if __name__ == "__main__":
	# initializing obj as Wordcount each time continues a running total
	# obj = WordCount("/Users/nikashtaskar/Library/Mobile Documents/com~apple~CloudDocs/College/Research/AMIA 2018/AMIA2019_ICU_Dashboard_final.txt")
	# obj.readInput()
	# obj.createDF()
	obj = WordCount("/Users/nikashtaskar/Library/Mobile Documents/com~apple~CloudDocs/College/Junior Year/Fall/Technical Writing/Research Paper.txt")
	obj.readInput()
	obj.createDF()

	obj.sigmoid()
	# print(obj.words)

	# add file path to line below
	# obj.readAndPredict(new file)
	
	




