import sha3
from os.path import commonprefix
import string
import random

print 'hello'



s = sha3.SHA3224() # also 224, 256, 384, 512
                   # also exposed as the function sha3.sha3_512(...)
s.update('112932095')
print(s.hexdigest())

s = sha3.SHA3224() 
s.update('112932099')
print(s.hexdigest())


dictionary ={}
dictionary['test'] = 1
print dictionary['test']

str1 = s.hexdigest()
str2 = s.hexdigest()
prefix = commonprefix([str1, str2])
#print prefix


numbers = {'first': 1, 'second': 2, 'third': 3, 'Fourth': 4}

hashList = []

testList = [ 1,2,4,5]
testList.insert(2,3)
#print testList




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



largestPrefix =0

def test(element):
	global largestPrefix
	index = insertIntoList(element)
	match, prefixSize = findLargestPrefix(element, index)
	if(prefixSize > largestPrefix):
		largestPrefix = prefixSize



def tailGenerator(size=50, chars=string.letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def generateRandomStrings(head):
	tailSize = random.randint(25,75)
	return head + tailGenerator(size = tailSize)



#insertIntoList(str122)
test("abcdz")
test("bad")
test("bba")
test("abcd")

#print hashList
#print largestPrefix
count = 0
while(count < 10):
	#print generateRandomStrings("112932095")
	count += 1








