import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('Johnson', 3, 1)

    def test_init(self):
        self.assertEqual('Johnson', self.room.family_name)
        self.assertEqual(3, self.room.budget)
        self.assertEqual(1, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_negative_expenses(self):
        with self.assertRaises(ValueError) as cm:
            self.room.expenses = -1
        self.assertEqual('Expenses cannot be negative', str(cm.exception))

if __name__ == '__main__':
    unittest.main()