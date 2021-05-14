def main():
	pal = input("Please enter a string: ")
	a = check(pal)
	print(a)


def check(pal):
	reverse = str(pal)[::-1]
	#print(reverse)
	#reverse = "dab"
	if(pal == reverse):
		return True
	else:
		return False

def test_pal():
	assert check(pal) == True

if __name__ == "__main__":
	main()
