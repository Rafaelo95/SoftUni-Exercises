from project.hardware.hardware import Hardware
import unittest
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('NVD', 'type', 10, 10)

    def test_init(self):
        self.assertEqual('NVD', self.hardware.name)
        self.assertEqual('type', self.hardware.type)
        self.assertEqual(10, self.hardware.capacity)
        self.assertEqual(10, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install(self):
        software = Software('MS', 'type', 5, 5)
        self.hardware.install(software)
        self.assertEqual(self.hardware.software_components, [software])

        software = Software('MS', 'type', 15, 15)
        with self.assertRaises(Exception) as cm:
            self.hardware.install(software)
        self.assertEqual(str(cm.exception), "Software cannot be installed")

    def test_uninstall(self):
        software = Software('MS', 'type', 5, 5)
        self.hardware.install(software)
        self.assertEqual(self.hardware.software_components, [software])
        self.hardware.uninstall(software)
        self.assertEqual(self.hardware.software_components, [])

if __name__ == '__main__':
    unittest.main()