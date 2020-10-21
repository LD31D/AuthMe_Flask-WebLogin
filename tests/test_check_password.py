import unittest
from utils.others.check_password import check_sha256


class TestSHA256Checker(unittest.TestCase):

	def test_right_password(self):
		trypass = '12345678'
		realpass = '$SHA$2d7a72eba4207d12$284b36e15a1960a7b4010bb23b1ff4971e558235b25dca64897294edf07b3280'
		self.assertTrue(check_sha256(trypass, realpass))

	def test_wrong_password(self):
		trypass = 'Password'
		realpass = '$SHA$2d7a72eba4207d12$284b36e15a1960a7b4010bb23b1ff4971e558235b25dca64897294edf07b3280'
		self.assertFalse(check_sha256(trypass, realpass))

	def test_invalid_value(self):
		with self.assertRaises(IndexError): 
			check_sha256('Password', "InvalidHash")

		with self.assertRaises(AttributeError): 
			check_sha256(1234, "$$$")

		with self.assertRaises(AttributeError): 
			check_sha256([], "$$$")

		with self.assertRaises(AttributeError): 
			check_sha256('Password', 1234)

