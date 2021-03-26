from project.player.beginner import Beginner
import unittest


class TestBeginner(unittest.TestCase):

    def test_if_init_is_properly_initialized(self):
        beginner = Beginner('Test')
        expected_name = 'Test'
        expected_hp = 50
        self.assertEqual(expected_hp, beginner.health)
        self.assertEqual(expected_name, beginner.username)
        self.assertFalse(beginner.is_dead)

    def test_username_raises_value_error(self):
        with self.assertRaises(ValueError) as context_manager:
            beginner = Beginner('')
        self.assertEqual('Player\'s username cannot be an empty string.', str(context_manager.exception))

    def test_health_raises_value_error(self):
        beginner = Beginner('John')
        with self.assertRaises(ValueError) as context_manager:
            beginner.health = -1
        self.assertEqual('Player\'s health bonus cannot be less than zero.', str(context_manager.exception))

    def test_is_dead(self):
        beginner = Beginner('John')
        self.assertFalse(beginner.is_dead)
        beginner.health = 0
        self.assertTrue(beginner.is_dead)

    def test_take_damage(self):
        beginner = Beginner('John')
        beginner.take_damage(10)
        self.assertEqual(40, beginner.health)

if __name__ == '__main__':
    unittest.main()