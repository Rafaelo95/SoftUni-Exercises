from project.card.magic_card import MagicCard
import unittest

class TestMagicCard(unittest.TestCase):

    def setUp(self):
        self.magic_card = MagicCard('Swords of Revealing Light')

    def test_if_init_is_properly_initialized(self):
        expected_name = "Swords of Revealing Light"
        expected_damage = 5
        expected_health = 80
        self.assertEqual(expected_name, self.magic_card.name)
        self.assertEqual(expected_damage, self.magic_card.damage_points)
        self.assertEqual(expected_health, self.magic_card.health_points)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as context_manager:
            magic_card = MagicCard('')
        self.assertEqual("Card's name cannot be an empty string.", str(context_manager.exception))

    def test_damage_less_than_zero(self):
        with self.assertRaises(ValueError) as context_manager:
            self.magic_card.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(context_manager.exception))

    def test_health_less_than_zero(self):
        with self.assertRaises(ValueError) as context_manager:
            self.magic_card.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(context_manager.exception))


if __name__ == '__main__':
    unittest.main()