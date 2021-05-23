import unittest
import leap_year

class Tester(unittest.TestCase):
  # Tests for valid leap years

  def test_right_1(self):
    self.assertEqual(leap_year.calc(2008), True)

  # Test for a year that is divisible by 100, but is divisible by 400.
  def test_right_2(self):
    self.assertEqual(leap_year.calc(2000), True)

  # Tests for invalid leap years

  def test_wrong_1(self):
    self.assertEqual(leap_year.calc(2021), False)
  
  # Test for a year that is divisible by 4, but is divisible by 100 but not 400.
  def test_wrong_2(self):
    self.assertEqual(leap_year.calc(1900), False)
  
  # Test for an invalid input type
  def test_type_error(self):
    with self.assertRaises(TypeError):
      leap_year.calc("hello")

if __name__ == '__main__':
  unittest.main()
