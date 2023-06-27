import unittest
import ValidateCreditCard


class TestValidateCreditCard(unittest.TestCase):

    def test_validate_credit_card(self):
        card_num = ValidateCreditCard.validate_credit_card_num("4321-5674-4908-7890")
        self.assertEqual(card_num, f"{'4321-5674-4908-7890'} is valid")

        card_num2 = ValidateCreditCard.validate_credit_card_num("1321-5674-4908-7890")
        self.assertEqual(card_num2, f"{'1321-5674-4908-7890'} is invalid")

if __name__ == "__main__":
    unittest.main()