from project.vehicle import Vehicle
import unittest


class TestingVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.00, 150.00)

    def test_if_init_is_properly_instantiated(self):
        self.assertEqual(self.vehicle.fuel, 20.0)
        self.assertEqual(self.vehicle.horse_power, 150.00)

    def test_drive_method_if_fuel_gets_reduced(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 7.5)

    def test_drive_method_if_fuel_is_enough(self):
        with self.assertRaises(Exception) as context_manager:
            self.vehicle.drive(100000000)
        self.assertEqual(str(context_manager.exception), 'Not enough fuel')

    def test_refuel_method_if_fuel_gets_increased(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 12.5)

    def test_refuel_if_fuel_is_too_much(self):
        with self.assertRaises(Exception) as context_manager:
            self.vehicle.refuel(100000000)
        self.assertEqual(str(context_manager.exception), 'Too much fuel')

    def test_if_str_method_returns_the_correct_string(self):
        expected = 'The vehicle has 150.0 horse power' \
                   ' with 20.0 fuel left and 1.25 fuel consumption'
        actual = self.vehicle.__str__()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()