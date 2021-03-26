from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
import unittest


class TestBattleField(unittest.TestCase):
    def test_att_is_dead(self):
        advanced = Advanced('test')
        advanced.health = 0
        advanced2 = Advanced('test2')
        battlefield = BattleField()
        with self.assertRaises(ValueError) as cm:
            battlefield.fight(advanced, advanced2)
        self.assertEqual('Player is dead!', str(cm.exception))

    def test_enemy_is_dead(self):
        advanced = Advanced('test')
        advanced2 = Advanced('test2')
        advanced2.health = 0
        battlefield = BattleField()
        with self.assertRaises(ValueError) as cm:
            battlefield.fight(advanced, advanced2)
        self.assertEqual('Player is dead!', str(cm.exception))

    def test_dmg_and_hp_without_cards(self):
        advanced = Advanced('test')
        beginner = Beginner('test2')
        battlefield = BattleField()
        battlefield.fight(advanced, beginner)
        self.assertEqual(advanced.health, 250)
        self.assertEqual(beginner.health, 90)

    def test_dmg_and_hp_with_cards(self):
        advanced = Advanced('test')
        beginner = Beginner('test2')
        battlefield = BattleField()
        magic_card = MagicCard('Light')
        trap_card = TrapCard('TRAP')

        advanced.card_repository.add(magic_card)
        beginner.card_repository.add(trap_card)

        battlefield.fight(advanced, beginner)
        self.assertEqual(advanced.health, 180)
        self.assertEqual(beginner.health, 90)


if __name__ == '__main__':
    unittest.main()