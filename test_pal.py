import unittest
import calc

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		result = calc.add(10,5)
		self.assertEqual(calc.add(10,5), 15)
	def test_add_2(self):
		self.assertEqual(calc.add(10,4), 15)

	def test_sub(self):
		self.assertEqual(calc.sub(10,5),5)
	def test_sub_2(self):
		self.assertEqual(calc.sub(10,4),5)

	def test_mul(self):
		self.assertEqual(calc.mul(5,5),25)
	def test_mul_2(self):
		self.assertEqual(calc.mul(10,3), 29)

	def test_div(self):
		self.assertEqual(calc.div(10, 5), 2)
	def test_div_2(self):
		self.assertEqual(calc.div(10, 5), 1)

#if __name__ = "__main__":
	#unittest.main()
