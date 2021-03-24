from project.hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.darlex = Hero("Darlex", 10, 100.0, 5.0)
        self.nartius = Hero("Nartius", 10, 50.0, 10.0)

    def test_if_init_is_properly_initialized(self):
        self.assertEqual(self.darlex.username, "Darlex")
        self.assertEqual(self.darlex.level, 10)
        self.assertEqual(self.darlex.health, 100.0)
        self.assertEqual(self.darlex.damage, 5.0)

    def test_if_hero_cannot_fight_self(self):
        other_darlex = Hero("Darlex", 1, 1.0, 1.0)
        with self.assertRaises(Exception) as context_manager:
            self.darlex.battle(other_darlex)
        self.assertEqual(str(context_manager.exception), "You cannot fight yourself")

    def test_if_self_health_is_less_than_or_equal_to_zero(self):
        self.darlex.health = 0
        with self.assertRaises(ValueError) as context_manager:
            self.darlex.battle(self.nartius)
        self.assertEqual(str(context_manager.exception), "Your health is lower than "
                                                         "or equal to 0. You need to rest")
        self.darlex.health = -5
        with self.assertRaises(ValueError) as context_manager:
            self.darlex.battle(self.nartius)
        self.assertEqual(str(context_manager.exception), "Your health is lower than "
                                                         "or equal to 0. You need to rest")

    def test_if_enemy_health_is_less_than_or_equal_to_zero(self):
        self.nartius.health = 0
        with self.assertRaises(ValueError) as context_manager:
            self.darlex.battle(self.nartius)
        self.assertEqual(str(context_manager.exception), f"You cannot fight"
                                                         f" {self.nartius.username}. "
                                                         f"He needs to rest")

        self.nartius.health = -5
        with self.assertRaises(ValueError) as context_manager:
            self.darlex.battle(self.nartius)
        self.assertEqual(str(context_manager.exception), f"You cannot fight"
                                                         f" {self.nartius.username}. "
                                                         f"He needs to rest")

    def test_if_player_damage_is_properly_calculated(self):
        self.darlex.battle(self.nartius)
        expected = 50.0
        actual = self.darlex.damage * self.darlex.level
        self.assertEqual(actual, expected)

    def test_if_enemy_hero_damage_is_properly_calculated(self):
        self.darlex.battle(self.nartius)
        expected = 100.0
        actual = self.nartius.damage * self.nartius.level
        self.assertEqual(actual, expected)

    def test_if_str_method_returns_correct_information(self):
        result = str(self.darlex)
        expected = f"Hero Darlex: 10 lvl\n" \
               f"Health: 100.0\n" \
               f"Damage: 5.0\n"
        self.assertEqual(result, expected)

    def test_if_battle_ends_in_draw(self):
        self.darlex.health = 1
        self.nartius.health = 1
        actual = self.darlex.battle(self.nartius)
        expected = "Draw"
        self.assertEqual(actual, expected)

    def test_if_enemy_hero_loses_and_if_main_hero_stats_are_increased(self):
        self.nartius.health = 1
        self.darlex.health = 101
        expected_level = self.darlex.level + 1
        expected_damage = self.darlex.damage + 5
        expected_health = 6.0
        actual = self.darlex.battle(self.nartius)
        expected_message = 'You win'
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.darlex.level, expected_level)
        self.assertEqual(self.darlex.health, expected_health)
        self.assertEqual(self.darlex.damage, expected_damage)

    def test_if_main_hero_loses_and_if_enemy_hero_stats_are_increased(self):
        self.nartius.health = 101
        self.darlex.health = 1
        expected_level = self.nartius.level + 1
        expected_damage = self.nartius.damage + 5
        expected_health = 56.0
        actual = self.darlex.battle(self.nartius)
        expected_message = 'You lose'
        self.assertEqual(actual, expected_message)
        self.assertEqual(self.nartius.level, expected_level)
        self.assertEqual(self.nartius.damage, expected_damage)
        self.assertEqual(self.nartius.health, expected_health)


if __name__ == "__main__":
    unittest.main()
