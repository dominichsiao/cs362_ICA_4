def main():
	word = input("Please enter a sentence: ")
	count(word)

def count(word):
	x = word.split()
	length = len(x)
	
	print(length)
	return length

#def main():
	#word = input("Please enter a sentence")
	#print(count(word)

if __name__ == "__main__":
	main()
