from project.player.advanced import Advanced
import unittest


class TestAdvanced(unittest.TestCase):

    def test_if_init_is_properly_initialized(self):
        advanced = Advanced('Test')
        expected_name = 'Test'
        expected_hp = 250
        self.assertEqual(expected_hp, advanced .health)
        self.assertEqual(expected_name, advanced.username)
        self.assertFalse(advanced.is_dead)

    def test_username_raises_value_error(self):
        with self.assertRaises(ValueError) as context_manager:
            advanced = Advanced('')
        self.assertEqual('Player\'s username cannot be an empty string.', str(context_manager.exception))

    def test_health_raises_value_error(self):
        advanced = Advanced('John')
        with self.assertRaises(ValueError) as context_manager:
            advanced.health = -1
        self.assertEqual('Player\'s health bonus cannot be less than zero.', str(context_manager.exception))

    def test_is_dead(self):
        advanced = Advanced('John')
        self.assertFalse(advanced.is_dead)
        advanced.health = 0
        self.assertTrue(advanced.is_dead)

    def test_take_damage(self):
        advanced = Advanced('John')
        advanced.take_damage(10)
        self.assertEqual(240, advanced.health)


if __name__ == '__main__':
    unittest.main()