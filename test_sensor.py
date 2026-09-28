import unittest
from sensor import read_moisture

class TestSensor(unittest.TestCase):
    def test_read_moisture_range(self):
        val = read_moisture()
        self.assertGreaterEqual(val, 30)
        self.assertLessEqual(val, 70)

if __name__ == "__main__":
    unittest.main()