import unittest
import word_count

class testCaseAdd(unittest.TestCase):
	def test_word(self):
		self.assertEqual(word_count.count("Hello from the other side"), 5)
	def test_word_2(self):
		self.assertEqual(word_count.count("I"), 1)

	def test_sub(self):
		self.assertEqual(word_count.count(""),0)

#if __name__ = "__main__":
	#unittest.main()
