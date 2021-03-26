from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
import unittest


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CardRepository()
        self.magic_card = MagicCard("Swords Of The Revealing Light")

    def test_if_init_is_properly_initialized(self):
        expected_count = 0
        expected_cards = []
        self.assertEqual(expected_cards, self.repository.cards)
        self.assertEqual(expected_count, self.repository.count)

    def test_if_add_function_raises_value_error_if_name_already_in_list(self):
        self.repository.add(self.magic_card)
        expected_result = "Card Swords Of The Revealing Light already exists!"
        with self.assertRaises(ValueError) as context_manager:
            self.repository.add(self.magic_card)
        self.assertEqual(expected_result, str(context_manager.exception))

    def test_if_add_function_adds_the_card_and_increases_the_count(self):
        self.repository.add(self.magic_card)
        expected_count = 1
        expected_cards = [self.magic_card]
        self.assertEqual(expected_count, self.repository.count)
        self.assertEqual(expected_cards, self.repository.cards)

    def test_if_remove_function_raises_value_error_with_empty_string(self):
        expected_result = "Card cannot be an empty string!"
        with self.assertRaises(ValueError) as context_manager:
            self.repository.remove('')
        self.assertEqual(expected_result, str(context_manager.exception))

    def test_if_remove_function_removes_the_card_and_decreases_the_count(self):
        second_magic_card = MagicCard('Something')
        expected_count = 1
        expected_cards = [self.magic_card]
        self.repository.add(self.magic_card)
        self.repository.add(second_magic_card)
        self.repository.remove('Something')
        self.assertEqual(expected_cards, self.repository.cards)
        self.assertEqual(expected_count, self.repository.count)

    def test_if_find_function_returns_the_object(self):
        self.repository.add(self.magic_card)
        expected_result = self.magic_card
        actual_result = self.repository.find('Swords Of The Revealing Light')
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()