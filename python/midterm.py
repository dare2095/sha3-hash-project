import sha3
from os.path import commonprefix
import string
import random
import sys

print "############ Beginning Project #################"


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
	return head + tailGenerator(size = 10)


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

def winnerFound(hString1, str1,  hString2, str2, prefixSize):
	global hashDictionary
	global win
	if(prefixSize > win.length):
		win.hashStr1 = hString1
		win.str1 = str1
		win.hashStr2 = hString2
		win.str2 = str2
		win.length = prefixSize
		win.bitLength = prefixSize * 4
		updateLogFile()

def getHash(inputString):
	s = sha3.SHA3224() 
	s.update(inputString)
	return s.hexdigest()

def getNextHare(inputString):
	return get


def main():
	global win
	global logFile
	print "beginning search..."

	logFile = sys.argv[1]
	if(logFile == ""):
		print "bad log file"
		return

	base = "112932095"
	primer = generateRandomString(base)
	print primer

	tortoise = getHash(primer)
	tortoiseString = primer

	hare1 = getHash(base + getHash(primer))
	hare1String = base + getHash(primer)

	hare2 = getHash(base + getHash(base + getHash(primer)))
	hare2String = base + getHash(base + getHash(primer))


	while True:

		prefix1 = len(commonprefix([ tortoise, hare1]))
		if(prefix1 > win.length):
			winnerFound(tortoise, tortoiseString, hare1, hare1String, prefix1)

		prefix2 = len(commonprefix([ tortoise, hare2]))
		if(prefix2 > win.length):
			winnerFound(tortoise, tortoiseString, hare2, hare2String, prefix2)

		#move tortoise one step
		tortoiseString = base + tortoise
		tortoise = getHash(base + tortoise)

		#move each hare two steps
		hare1String = base + getHash(base + hare1)
		hare1 = getHash(base + getHash(base + hare1))

		hare2String = base + getHash(base + hare2)
		hare2 = getHash(base + getHash(base + hare2))














main()









