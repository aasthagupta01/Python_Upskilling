import unittest
import AlphanumericSorting

class TestAlphanumericSorting(unittest.TestCase):
    def test_alphanumeric_sorting(self):
        num1 = AlphanumericSorting.alphanumeric_sorting("ABcd1234")
        self.assertEqual(num1, "cdAB1324")

        num2 = AlphanumericSorting.alphanumeric_sorting("AZcr2315")
        self.assertEqual(num2, "crAZ1352")

if __name__ == "__main__":
    unittest.main()
