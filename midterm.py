import sha3
from os.path import commonprefix
import string
import random
import sys

print "############ Beginning Project #################"

hashList = []

# { hash, input }
hashDictionary = {}

logFile = ""

class Winner:
	str1 = ""
	str2 = ""
	hashStr1 = ""
	hashStr2 = ""
	length = 0
	bitLength = 0

win = Winner()


def tailGenerator(size=50, chars=string.letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def generateRandomString(head):
	tailSize = random.randint(25,75)
	return head + tailGenerator(size = tailSize)

def insertIntoList(element):
	global hashList
	if(len(hashList) == 0):
		hashList.append(element)
		return 0
	else:
		index = 0
		while(index < len(hashList)):
			if(element < hashList[index]):
				hashList.insert(index, element)
				return index
			index += 1
		hashList.append(element)
		return index

def findLargestPrefix(element, index):
	global hashList
	best = 0
	match = element
	if(index > 0):
		previous = hashList[index -1]
		length1 = len(commonprefix([previous, element]))
		if(length1 > best and element != previous): 
			best = length1
			match = previous
	if(index < len(hashList) -1):
		forwards = hashList[index +1]
		length2 = len(commonprefix([element, forwards]))
		if(length2 > best and element != forwards): 
			best = length2
			match = forwards
	return match, best


def updateLogFile():
	global win
	global logFile
	print ("\n########### NEW WINNER FOUND #############\n")
	print ("\n" + win.str1 + "   <==>  " + win.hashStr1)
	print ("\n" + win.str2 + "   <==>  " + win.hashStr2)
	print ("\n  prefix length: " + str(win.length) + "  or  " + str(win.bitLength) + "  bits \n\n")
	with open(logFile, "a") as file:
		file.write("\n########### NEW WINNER FOUND #############\n")
		file.write("\n" + win.str1 + "   <==>  " + win.hashStr1)
		file.write("\n" + win.str2 + "   <==>  " + win.hashStr2)
		file.write("\n  prefix length: " + str(win.length) + "  or  " + str(win.bitLength) + "  bits\n\n")
		file.close()

def winnerFound(hString1, hString2, prefixSize):
	global hashDictionary
	global win
	if(prefixSize > win.length):
		win.hashStr1 = hString1
		win.str1 = hashDictionary[hString1]
		win.hashStr2 = hString2
		win.str2 = hashDictionary[hString2]
		win.length = prefixSize
		win.bitLength = prefixSize * 4
		updateLogFile()




def main():
	global hashList
	global hashDictionary
	global win
	global logFile
	print "beginning search..."

	logFile = sys.argv[1]
	if(logFile == ""):
		print "bad log file"
		return

		
	counter =0
	while True:
		counter+=1
		inputString = generateRandomString("112932095") # get input string
		s = sha3.SHA3224() # create hash object
		s.update(inputString) 
		hashString = s.hexdigest() # get hash string

		# update the hash dictionary
		hashDictionary[hashString] = inputString

		#insert into list
		index = insertIntoList(hashString)

		#find its largest prefix
		match, prefixSize = findLargestPrefix(hashString, index)

		if(prefixSize > win.length and match != hashString):
			winnerFound(hashString, match, prefixSize)




main()









