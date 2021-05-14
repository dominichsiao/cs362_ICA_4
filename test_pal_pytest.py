import pytest
import palindrome

#class TestPal:
def test_palindrome():
	assert palindrome.check ("pip") == True

def test_palindrome_1():
	assert palindrome.check ("kayak") == True

def test_palindrome_Case_Sense():
	assert palindrome.check ("Dad") == True

def test_palindrome_Fail():
	assert palindrome.check ("palindrome") == False
	
