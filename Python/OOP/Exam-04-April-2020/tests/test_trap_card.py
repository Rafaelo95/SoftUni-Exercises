from project.card.trap_card import TrapCard
import unittest

class TestTrapCard(unittest.TestCase):

    def setUp(self):
        self.trap_card = TrapCard('Swords of Revealing Light')

    def test_if_init_is_properly_initialized(self):
        expected_name = "Swords of Revealing Light"
        expected_damage = 120
        expected_health = 5
        self.assertEqual(expected_name, self.trap_card.name)
        self.assertEqual(expected_damage, self.trap_card.damage_points)
        self.assertEqual(expected_health, self.trap_card.health_points)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as context_manager:
            t = TrapCard('')
        self.assertEqual("Card's name cannot be an empty string.", str(context_manager.exception))

    def test_damage_less_than_zero(self):
        with self.assertRaises(ValueError) as context_manager:
            self.trap_card.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(context_manager.exception))

    def test_health_less_than_zero(self):
        with self.assertRaises(ValueError) as context_manager:
            self.trap_card.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(context_manager.exception))


if __name__ == '__main__':
    unittest.main()