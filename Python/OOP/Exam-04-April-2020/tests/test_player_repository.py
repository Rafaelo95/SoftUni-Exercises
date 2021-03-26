from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner
import unittest

class TestPlayerRepository(unittest.TestCase):

    def setUp(self):
        self.repository = PlayerRepository()
        self.beginner = Beginner('John')

    def test_if_init_is_set_properly(self):
        expected_count = 0
        expected_players = []
        self.assertEqual(expected_count, self.repository.count)
        self.assertEqual(expected_players, self.repository.players)

    def test_if_add_function_raises_value_error_if_player_is_already_in_list(self):
        self.repository.players = [self.beginner]
        with self.assertRaises(ValueError) as context_manager:
            self.repository.add(self.beginner)
        expected_message = f"Player John already exists!"
        self.assertEqual(expected_message, str(context_manager.exception))

    def test_if_add_function_appends_and_increases_count(self):
        self.repository.add(self.beginner)
        expected_result_for_players_list = [self.beginner]
        expected_result_for_count = 1
        self.assertEqual(expected_result_for_count, self.repository.count)
        self.assertEqual(expected_result_for_players_list, self.repository.players)

    def test_if_remove_function_raises_value_error(self):
        expected_result = "Player cannot be an empty string!"
        with self.assertRaises(ValueError) as context_manager:
            self.repository.remove('')
        self.assertEqual(expected_result, str(context_manager.exception))

    def test_if_remove_function_removes_player_and_decreases_count(self):
        self.repository.players = [self.beginner]
        self.repository.count = 1
        self.repository.remove('John')
        expected_count = 0
        expected_list = []
        self.assertEqual(expected_count, self.repository.count)
        self.assertEqual(expected_list, self.repository.players)

    def test_if_find_function_works(self):
        self.repository.players = [self.beginner]
        result = self.repository.find('John')
        expected_result = self.beginner
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()