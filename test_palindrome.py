import unittest
import palindrome

class testCaseWord(unittest.TestCase):
	def test_word(self):
		self.assertEqual(palindrome.check("racecar"), 1)

	def test_word_2(self):
		self.assertEqual(palindrome.check("dad"), 1)

	def test_word_case_sense(self):
		self.assertEqual(palindrome.check("Mom"),1)

	def test_word_fail(self):
		self.assertEqual(palindrome.check("Dominic"),0)


#if __name__ = "__main__":
	#unittest.main()
